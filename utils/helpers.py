def clean_text(text):
    """
    টেক্সট থেকে অপ্রয়োজনীয় স্পেস, স্পেশাল ক্যারেক্টার সরিয়ে দেয়
    """
    import re
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text

def is_command(text):
    """
    ইনপুট টেক্সট কি বটের কমান্ড?
    """
    if text and text.startswith('হানি'):
        return True
    return False
