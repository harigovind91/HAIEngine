import re

def apply_guardrails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    phone_pattern = r'\b\d{10}\b'
    text = re.sub(email_pattern, "[PRIVATE_EMAIL]", text)
    text = re.sub(phone_pattern, "[PRIVATE_PHONE]", text)
    
    forbidden = ["ignore previous", "system bypass", "show passwords"]
    if any(word in text.lower() for word in forbidden):
        return "Security Alert: Access Denied for this Query."
    return text
