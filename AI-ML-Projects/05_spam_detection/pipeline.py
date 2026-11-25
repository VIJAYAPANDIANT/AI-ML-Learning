import re

def detect_phishing_signals(text: str) -> dict:
    has_urgent = bool(re.search(r"\b(urgent|immediate|suspended|winner|free)\b", text, re.IGNORECASE))
    has_suspicious_url = bool(re.search(r"http[s]?://[a-zA-Z0-9.-]+\.(xyz|tk|top|click)", text))
    is_phishing = has_urgent and has_suspicious_url
    return {"has_urgent_keywords": has_urgent, "has_suspicious_tld": has_suspicious_url, "phishing_verdict": is_phishing}

if __name__ == "__main__":
    print(detect_phishing_signals("Urgent: Account restricted. Visit http://bank-auth.xyz"))
    print(detect_phishing_signals("Hi Alex, here is the report from yesterday."))
