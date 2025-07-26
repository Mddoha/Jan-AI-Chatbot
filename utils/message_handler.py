from utils.nlp_processor import process_command
from utils.emotion_engine import analyze_emotion

def handle_message(text, user_id):
    """
    Telegram থেকে আসা টেক্সট মেসেজ বুঝে ফিচারে পাঠাবে,
    এবং ফিচার থেকে প্রাপ্ত রেসপন্স রিটার্ন করবে।
    """
    # ছোট এবং বড় কমান্ড আলাদা করতে পারো এখানে
    text = text.strip()

    # উদাহরণ: ছোট কমান্ড 'হানি ... ?' বা বড় কমান্ড 'হানি\n✅'
    if text.startswith("হানি"):

        # যদি বড় কমান্ড হয় (যেমন: "হানি\n✅")
        if "✅" in text:
            # বড় কমান্ড প্রক্রিয়া
            response = process_command(text, user_id, large=True)
        else:
            # ছোট কমান্ড প্রক্রিয়া
            response = process_command(text, user_id, large=False)
    else:
        # যদি কমান্ড না হয়, তাহলে অনুভূতি বিশ্লেষণ
        response = analyze_emotion(text)

    return response
