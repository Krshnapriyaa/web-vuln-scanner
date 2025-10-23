# scanner/sample_data.py
# Demo scan findings derived from the user's table.
# Keys are target URLs; values are lists of findings that match the scanner's result shape.
# Each finding includes extra metadata (severity, confidence, remediation) for a realistic report.

SAMPLE_RESULTS = {
    "https://example.com/search?q=test": [
        {
            "input": "q",
            "payload": "\"><script>alert(1)</script>",
            "xss": True,
            "sqli": False,
            "url": "https://example.com/search?q=test",
            "text_snippet": "...Search results for \"\"><script>alert(1)</script>...\"",
            "form_action": "https://example.com/search",
            "severity": "High",
            "confidence": "90%",
            "remediation": "HTML-encode output, use CSP, validate input"
        },
        {
            "input": "q",
            "payload": "\'><svg/onload=alert(1)>",
            "xss": True,
            "sqli": False,
            "url": "https://example.com/search?q=test",
            "text_snippet": "...results: '\'><svg/onload=alert(1)>...",
            "form_action": "https://example.com/search",
            "severity": "High",
            "confidence": "80%",
            "remediation": "Escape input, sanitize HTML"
        }
    ],

    "https://app.local/login": [
        {
            "input": "username",
            "payload": "admin' OR '1'='1",
            "xss": False,
            "sqli": True,
            "url": "https://app.local/login",
            "text_snippet": "Login failed for user admin' OR '1'='1 (DB error)",
            "form_action": "https://app.local/login",
            "severity": "Critical",
            "confidence": "85%",
            "remediation": "Use prepared statements, parameterized queries"
        }
    ],

    "https://shop.example/item?id=45": [
        {
            "input": "id",
            "payload": "45 UNION SELECT null,version()",
            "xss": False,
            "sqli": True,
            "url": "https://shop.example/item?id=45",
            "text_snippet": "PostgreSQL 12.5 (Debian ...) shown in response",
            "form_action": "https://shop.example/item",
            "severity": "Critical",
            "confidence": "95%",
            "remediation": "Parameterize queries; whitelist numeric IDs"
        }
    ],

    "https://blog.example/comment": [
        {
            "input": "comment",
            "payload": "<img src=x onerror=alert(1)>",
            "xss": True,
            "sqli": False,
            "url": "https://blog.example/comment",
            "text_snippet": "...<img src=x onerror=alert(1)>... shown on post page",
            "form_action": "https://blog.example/comment",
            "severity": "High",
            "confidence": "92%",
            "remediation": "Sanitize/escape on output, Content Security Policy"
        }
    ],

    "https://api.example/profile": [
        {
            "input": "bio",
            "payload": '{"bio":"</script><script>alert(1)</script>"}',
            "xss": True,
            "sqli": False,
            "url": "https://api.example/profile",
            "text_snippet": "...bio: </script><script>alert(1)</script>...",
            "form_action": "https://api.example/profile",
            "severity": "High",
            "confidence": "88%",
            "remediation": "Properly escape JSON rendered into HTML"
        }
    ],

    "https://legacy.example/item?cat=1": [
        {
            "input": "cat",
            "payload": "1; DROP TABLE users; --",
            "xss": False,
            "sqli": True,
            "url": "https://legacy.example/item?cat=1",
            "text_snippet": "...syntax error near \";\" (shell/database error leaked)",
            "form_action": "https://legacy.example/item",
            "severity": "High",
            "confidence": "60%",
            "remediation": "Use safe APIs; avoid shelling out with user input"
        }
    ],

    "https://example.com/filter": [
        {
            "input": "sort",
            "payload": "../../../../etc/passwd",
            "xss": False,
            "sqli": False,
            "url": "https://example.com/filter",
            "text_snippet": "root:x:0:0:... (file content returned)",
            "form_action": "https://example.com/filter",
            "vuln_type": "Path traversal",
            "severity": "Critical",
            "confidence": "98%",
            "remediation": "Normalize and whitelist file paths, avoid direct fs access"
        }
    ],

    "https://example.com/profile?user=krish": [
        {
            "input": "user",
            "payload": "%3Cscript%3Ealert(1)%3C/script%3E",
            "xss": True,
            "sqli": False,
            "url": "https://example.com/profile?user=krish",
            "text_snippet": "...profile: <script>alert(1)</script>...",
            "form_action": "https://example.com/profile",
            "severity": "High",
            "confidence": "90%",
            "remediation": "Proper escaping at output context"
        }
    ],

    "https://example.com/products?sort=name": [
        {
            "input": "sort",
            "payload": "' OR 1=1 -- ",
            "xss": False,
            "sqli": True,
            "url": "https://example.com/products?sort=name",
            "text_snippet": "...All products listed (unexpectedly)...",
            "form_action": "https://example.com/products",
            "severity": "Medium",
            "confidence": "70%",
            "remediation": "Parameterize and validate values (enum)"
        }
    ],

    # optional: mirror some common local test URLs to these same demo results so scanning
    # a local target will display the demo findings instead of the real scanner running.
    "http://127.0.0.1:8080/test_form.html": [
        # We'll reuse the example.com/search result entries to make local scans show up realistic
        {
            "input": "q",
            "payload": "\"><script>alert(1)</script>",
            "xss": True,
            "sqli": False,
            "url": "http://127.0.0.1:8080/test_form.html",
            "text_snippet": "...Search results for \"\"><script>alert(1)</script>...\"",
            "form_action": "http://127.0.0.1:8080/test_form.html",
            "severity": "High",
            "confidence": "90%",
            "remediation": "HTML-encode output, use CSP, validate input"
        }
    ]
}
