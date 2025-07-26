import requests
import base64
from config import GITHUB_TOKEN, GITHUB_REPO, OWNER_UID

GITHUB_API_URL = "https://api.github.com"

def create_github_file(path, content, message, user_id):
    """
    GitHub এ নতুন ফাইল তৈরি করে বা আপডেট করে
    """
    if user_id != OWNER_UID:
        return "❌ আপনি এই ফিচার ব্যবহারের অনুমতি পাচ্ছেন না।"

    url = f"{GITHUB_API_URL}/repos/{GITHUB_REPO}/contents/{path}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    # আগে ফাইল আছে কিনা চেক করি
    get_resp = requests.get(url, headers=headers)
    sha = None
    if get_resp.status_code == 200:
        sha = get_resp.json().get("sha")

    data = {
        "message": message,
        "content": base64.b64encode(content.encode()).decode(),
        "branch": "main"
    }
    if sha:
        data["sha"] = sha  # যদি ফাইল থাকে, তাহলে আপডেট

    put_resp = requests.put(url, headers=headers, json=data)
    if put_resp.status_code in [200, 201]:
        return "✅ GitHub ফাইলে সফলভাবে আপলোড করা হয়েছে।"
    else:
        return f"❌ আপলোডে সমস্যা হয়েছে: {put_resp.text}"
