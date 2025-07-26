import time
import requests
from utils.config_loader import load_config
from utils.auth_filter import is_authorized_user
from utils.message_handler import handle_message
from utils.logger import setup_logging
from utils.self_checker import run_self_test
from utils.auto_updater import check_for_updates
from utils.error_recovery import try_alternatives
from utils.language_tone import apply_poetic_tone
from utils.watchdog import keep_alive

# config.json থেকে সেটিংস লোড
config = load_config("config.json")
TELEGRAM_TOKEN = config.get("TELEGRAM_TOKEN")
OWNER_UID = config.get("OWNER_UID")
CEO_UID = config.get("CEO_UID")
ADMIN_UIDS = config.get("ADMIN_UIDS", [])

TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

def get_updates(offset=None):
    try:
        params = {"timeout": 100, "offset": offset}
        response = requests.get(f"{TELEGRAM_API_URL}/getUpdates", params=params)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"❌ আপডেট আনার সময় ত্রুটি: {e}")
    return None

def send_message(chat_id, text):
    try:
        poetic_reply = apply_poetic_tone(text)
        payload = {
            "chat_id": chat_id,
            "text": poetic_reply,
            "parse_mode": "Markdown"
        }
        requests.post(f"{TELEGRAM_API_URL}/sendMessage", data=payload)
    except Exception as e:
        print(f"❌ মেসেজ পাঠাতে ব্যর্থ: {e}")

def main():
    print("✨ Jan-AI-Chatbot কবিতার ছন্দে জেগে উঠেছে... সবসময় জাগ্রত...")

    offset = None

    # নিজের শরীর-মন পরীক্ষা করে নেয়
    run_self_test()

    # নতুন আপডেট খোঁজে নেয়
    check_for_updates()

    while True:
        updates = get_updates(offset)
        if updates and updates.get("result"):
            for item in updates["result"]:
                offset = item["update_id"] + 1
                message = item.get("message")

                if message:
                    user_id = message["from"]["id"]
                    chat_id = message["chat"]["id"]
                    text = message.get("text", "")

                    # অনুমোদিত ইউজার কিনা যাচাই
                    if is_authorized_user(user_id):
                        try:
                            response = handle_message(text, user_id)
                            send_message(chat_id, response)
                        except Exception:
                            # ব্যর্থ হলে বিকল্প চেষ্টা
                            fallback = try_alternatives(text)
                            send_message(chat_id, fallback)
                    else:
                        send_message(chat_id, "⚠️ দুঃখিত প্রিয়, আপনি এখনো আমাদের অনুমোদিত অতিথি নন।")

        # বট বেঁচে আছে তা নিশ্চিত করে
        keep_alive()
        time.sleep(1)

if __name__ == "__main__":
    main()
