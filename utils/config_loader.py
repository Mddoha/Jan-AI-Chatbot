import json

try:
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    TELEGRAM_TOKEN = config.get("TELEGRAM_TOKEN")
    OWNER_UID = config.get("OWNER_UID")
    CEO_UID = config.get("CEO_UID")
    ADMIN_UIDS = config.get("ADMIN_UIDS", [])

    GITHUB_TOKEN = config.get("GITHUB_TOKEN")
    GITHUB_REPO = config.get("GITHUB_REPO")

    BLOGGER_CLIENT_ID = config.get("BLOGGER_CLIENT_ID")
    BLOGGER_CLIENT_SECRET = config.get("BLOGGER_CLIENT_SECRET")
    BLOGGER_REFRESH_TOKEN = config.get("BLOGGER_REFRESH_TOKEN")

except Exception as e:
    print(f"⚠️ কনফিগ লোডিং সমস্যা: {e}")
