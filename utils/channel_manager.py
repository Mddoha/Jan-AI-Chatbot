import requests
from config import TELEGRAM_TOKEN

TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

def get_chat_admins(chat_id):
    """
    কোন চ্যানেলে আপনি অ্যাডমিন কিনা তা যাচাই করতে পারে
    """
    url = f"{TELEGRAM_API_URL}/getChatAdministrators"
    params = {"chat_id": chat_id}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json().get("result", [])
    return []

def is_user_admin(chat_id, user_id):
    """
    একজন ইউজার অ্যাডমিন কিনা চেক করে
    """
    admins = get_chat_admins(chat_id)
    for admin in admins:
        if admin["user"]["id"] == user_id:
            return True
    return False
