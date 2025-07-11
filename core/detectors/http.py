import requests

def scan(target):
    try:
        r = requests.get(target, timeout=5)
        if "honeypot" in r.text.lower() or r.status_code in [403, 429]:
            return {"status": "honeypot-suspected", "code": r.status_code}
        return {"status": "clean", "code": r.status_code}
    except Exception as e:
        return {"status": "error", "error": str(e)}