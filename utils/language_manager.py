def detect_language(text):
    """
    খুব সহজে ইংরেজি এবং বাংলা টেক্সট শনাক্ত করবে।
    তোমার NLP প্রসেসর বা হ্যান্ডলারে ব্যবহার করো।
    """
    # যদি বাংলা অক্ষর থাকে, তাহলে বাংলা
    for ch in text:
        if '\u0980' <= ch <= '\u09FF':
            return "bn"
    # অন্যথায় ইংরেজি ধরে নেবে
    return "en"

def get_response_in_language(response_bn, response_en, user_text):
    lang = detect_language(user_text)
    if lang == "bn":
        return response_bn
    else:
        return response_en
