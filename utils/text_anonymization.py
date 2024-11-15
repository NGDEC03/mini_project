import re

def anonymize_text(text):
    text = re.sub(r'\b(\w+\.\w+@\w+\.\w+)\b', 'email_removed', text)
    text = re.sub(r'\b\d{10}\b', 'phone_removed', text)
    return text
