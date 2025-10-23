import requests
from copy import deepcopy
from .detectors import detect_xss, detect_sqli

def submit_form(session, form, payloads):
    action = form['action']
    method = form['method']
    base_data = {inp['name']: inp.get('value', '') or 'test' for inp in form['inputs'] if inp.get('name')}
    results = []
    # baseline response (without payload) could be captured here if desired
    for name in list(base_data.keys()):
        for pl in payloads:
            data = deepcopy(base_data)
            data[name] = pl
            try:
                if method == 'post':
                    r = session.post(action, data=data, timeout=10)
                else:
                    r = session.get(action, params=data, timeout=10)
            except Exception as e:
                continue
            res = {"input": name, "payload": pl, "status": r.status_code, "text_snippet": r.text[:300], "url": r.url}
            res["xss"] = detect_xss(r, pl)
            res["sqli"] = detect_sqli(r, pl)
            results.append(res)
    return results
