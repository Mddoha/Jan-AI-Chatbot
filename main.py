import requests
import json
from utils.message_handler import handle_message
from utils.auth_filter import is_authorized_user
from config import TELEGRAM_TOKEN, OWNER_UID

TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

def get_updates(offset=None):
    params = {"timeout": 100, "offset": offset}
    resp = requests.get(f"{TELEGRAM_API_URL}/getUpdates", params=params)
    if resp.status_code == 200:
        return resp.json()
    return None

def send_message(chat_id, text):
    data = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
    requests.post(f"{TELEGRAM_API_URL}/sendMessage", data=data)

def main():
    print("Jan-AI-Chatbot is running...")
    offset = None

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

                    if is_authorized_user(user_id):
                        response = handle_message(text, user_id)
                        send_message(chat_id, response)
                    else:
                        send_message(chat_id, "দুঃখিত, আপনি অনুমোদিত ইউজার নন।")

if __name__ == "__main__":
    main()
