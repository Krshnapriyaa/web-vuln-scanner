import re

def detect_xss(response, payload):
    try:
        body = response.text
        # reflected XSS if payload appears in response body
        if payload in body:
            return True
        # fallback regex match
        if re.search(re.escape(payload), body):
            return True
    except Exception:
        return False
    return False

def detect_sqli(response, payload):
    errors = [
        "you have an error in your sql syntax",
        "mysql",
        "sqlstate",
        "syntax error",
        "warning: sqlite3"
    ]
    try:
        body = response.text.lower()
        for e in errors:
            if e in body:
                return True
    except Exception:
        return False
    return False

def has_csrf_token(form):
    token_names = ['csrfmiddlewaretoken', 'csrf_token', '_csrf', 'authenticity_token']
    for inp in form.get('inputs', []):
        if inp.get('name') and inp['name'].lower() in token_names:
            return True
    return False
