import random

def emotion_based_response(text):
    """
    ইউজারের কথার উপর ভিত্তি করে সাধারণ আবেগনির্ভর রেসপন্স তৈরি করে।
    """

    positive_keywords = ["ভালো", "দারুন", "ধন্যবাদ", "সুন্দর"]
    negative_keywords = ["খারাপ", "বিরক্ত", "ভয়ংকর", "দুঃখ"]

    lower_text = text.lower()

    if any(word in lower_text for word in positive_keywords):
        responses = [
            "😊 শুনে ভালো লাগলো!",
            "🌟 ধন্যবাদ! আপনি খুবই পজিটিভ!",
            "🥰 আমিও ঠিক তাই ভাবছিলাম!"
        ]
    elif any(word in lower_text for word in negative_keywords):
        responses = [
            "😢 দুঃখিত, আমি পাশে আছি।",
            "🫂 যদি কিছু বলো, শোনার জন্য আছি।",
            "😞 ঠিক আছে, সব ঠিক হয়ে যাবে!"
        ]
    else:
        responses = [
            "🤔 একটু বিস্তারিত বলো, বুঝতে চেষ্টা করছি।",
            "🧠 আমি শুনছি…",
            "🙃 কেমন চলছে দিনকাল?"
        ]

    return random.choice(responses)
