# Non-destructive example payloads for learning/detection only
XSS_PAYLOADS = [
    "<script>alert(1337)</script>",
    "'\"><img src=x onerror=alert(1)>"
]

SQLI_PAYLOADS = [
    "' OR '1'='1",
    "' OR SLEEP(5)--"
]
