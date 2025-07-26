import random

# বাংলা সাহিত্যিক ভঙ্গিতে বাক্য সাজানোর ফাংশন
def poetic_bangla_tone(text):
    poetic_starters = [
        "হে প্রিয় মানুষ,",
        "মন ছুঁয়ে যাওয়া এক কথা,",
        "তোমার উদ্দেশে বলি—",
        "স্মৃতির পাতায় লেখা হোক,",
        "জীবনের গোপন জানালায়—",
    ]
    poetic_endings = [
        "— এ যেন মনের গভীর আর্তনাদ।",
        "এই বাক্যে হয়তো কিছু কবিতা জেগে উঠেছে।",
        "ভালো থেকো শব্দের ছায়ায়।",
        "ভাষা যেখানে হার মানে, অনুভূতি সেখানে কথা বলে।",
        "এই হলো আজকের ভাষ্য।",
    ]
    starter = random.choice(poetic_starters)
    ending = random.choice(poetic_endings)
    return f"{starter} {text.strip()} {ending}"

# ইংরেজি বা অন্য ভাষায় অনুবাদ Placeholder (বিকল্পে DeepL/Google API ব্যবহার করা যায়)
def translate_to_language(text, lang="en"):
    if lang == "en":
        return f"[English Translation] {text}"
    elif lang == "hi":
        return f"[हिंदी अनुवाद] {text}"
    else:
        return f"[{lang} ভাষার অনুবাদ নেই] {text}"

# ভাষা ও স্বর অনুযায়ী বেছে নেওয়া ফাংশন
def respond_in_style(text, lang="bn"):
    if lang == "bn":
        return poetic_bangla_tone(text)
    else:
        return translate_to_language(text, lang)
