from utils.nlp_processor import process_command
from utils.emotion_engine import emotion_based_response

def handle_message(text, user_id):
    """
    টেলিগ্রাম থেকে আসা মেসেজ বুঝে প্রক্রিয়া করে রেসপন্স তৈরি করে।
    """

    text = text.strip()

    if text.startswith("হানি"):

        if "✅" in text:
            # বড় কমান্ড হলে
            response = process_command(text, user_id, large=True)
        else:
            # ছোট কমান্ড হলে
            response = process_command(text, user_id, large=False)
    else:
        # অন্য যেকোনো মেসেজ হলে আবেগ ভিত্তিক উত্তর
        response = emotion_based_response(text)

    return response
