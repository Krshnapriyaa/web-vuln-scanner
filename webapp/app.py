from flask import Flask, request, render_template, redirect, url_for
from scanner.crawler import Crawler
from scanner.form_parser import parse_forms
from scanner.injector import submit_form
from scanner.payloads import XSS_PAYLOADS, SQLI_PAYLOADS
from scanner.logger import save_report
from scanner.sample_data import SAMPLE_RESULTS
import requests

app = Flask(__name__)
scans = {}

def find_demo_report_for_target(target: str):
    """
    Try to find a demo report that matches the exact target,
    or where the sample key is a prefix of the target (helps match URLs
    that contain query strings or slightly different host syntax).
    Returns the list of findings or None.
    """
    # exact match
    if target in SAMPLE_RESULTS:
        return SAMPLE_RESULTS[target]

    # try to match ignoring small variations: sample_key is prefix of target
    for sample_key, findings in SAMPLE_RESULTS.items():
        if target.startswith(sample_key) or sample_key.startswith(target):
            return findings
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        target = request.form['target'].strip()
        if not target.startswith('http'):
            target = 'http://' + target

        # --- demo-mode: use built-in sample results if a matching key exists ---
        demo_report = find_demo_report_for_target(target)
        if demo_report is not None:
            report = demo_report
            scans[target] = report
            save_report(report)  # save a server-side copy as before
            return redirect(url_for('results') + f'?target={target}')

        # --- otherwise run the normal scanner as before ---
        crawler = Crawler(target, max_pages=20)
        pages = crawler.crawl()
        session = requests.Session()
        report = []
        for url, html in pages:
            forms = parse_forms(url, html)
            for f in forms:
                res = submit_form(session, f, XSS_PAYLOADS + SQLI_PAYLOADS)
                # enrich with form action
                for r in res:
                    r['form_action'] = f.get('action')
                report.extend(res)
        scans[target] = report
        saved = save_report(report)
        return redirect(url_for('results') + f'?target={target}')

    return render_template('index.html')

@app.route('/results')
def results():
    target = request.args.get('target')
    report = scans.get(target, [])
    return render_template('results.html', target=target, report=report)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
