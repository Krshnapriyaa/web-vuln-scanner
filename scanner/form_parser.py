from bs4 import BeautifulSoup
from urllib.parse import urljoin

def parse_forms(page_url, html):
    soup = BeautifulSoup(html, "lxml")
    forms = []
    for f in soup.find_all("form"):
        action = f.get("action")
        method = (f.get("method") or "get").lower()
        action = urljoin(page_url, action) if action else page_url
        inputs = []
        for inp in f.find_all(["input", "textarea", "select"]):
            name = inp.get("name")
            input_type = inp.get("type", "text")
            value = inp.get("value", "")
            inputs.append({"name": name, "type": input_type, "value": value})
        forms.append({"action": action, "method": method, "inputs": inputs})
    return forms
