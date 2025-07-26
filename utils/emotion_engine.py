def detect_emotion(text):
    """
    ইউজারের মেসেজ থেকে সহজভাবে আবেগ (emotion) চিহ্নিত করে।
    """

    lowered = text.lower()
    if any(word in lowered for word in ["ভালো", "সুন্দর", "চমৎকার", "thanks", "thank you", "ধন্যবাদ"]):
        return "😊 আপনার মেসেজ শুনে ভালো লাগলো!"
    elif any(word in lowered for word in ["দুঃখ", "খারাপ", "মাথা গরম", "রাগ", "কষ্ট"]):
        return "😔 আমি দুঃখিত আপনি এমন অনুভব করছেন। আমি পাশে আছি!"
    elif "?" in text:
        return "🤔 প্রশ্ন মনে হচ্ছে... দেখি বুঝি কী বলা যায়!"
    else:
        return "🙂 ঠিক আছে, আমি প্রসেস করছি..."

def emotion_based_response(text):
    """
    আবেগ বিশ্লেষণ করে আরও মানবিক রিপ্লাই তৈরি করে দেয়।
    """
    emotion_msg = detect_emotion(text)
    return f"{emotion_msg}\n\nআপনার মেসেজ ছিল:\n{text}"
