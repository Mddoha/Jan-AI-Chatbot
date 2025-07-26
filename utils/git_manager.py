import subprocess
import base64
import requests
from config import GITHUB_TOKEN, GITHUB_REPO, OWNER_UID

GITHUB_API_URL = "https://api.github.com"

def is_owner(user_id):
    return user_id == OWNER_UID

def get_file_sha(path):
    url = f"{GITHUB_API_URL}/repos/{GITHUB_REPO}/contents/{path}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("sha")
    return None

def upload_file(path, content, commit_message, user_id):
    if not is_owner(user_id):
        return "❌ আপনার অনুমতি নেই।"

    sha = get_file_sha(path)
    data = {
        "message": commit_message,
        "content": base64.b64encode(content.encode()).decode(),
        "branch": "main"
    }
    if sha:
        data["sha"] = sha

    url = f"{GITHUB_API_URL}/repos/{GITHUB_REPO}/contents/{path}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.put(url, headers=headers, json=data)

    if response.status_code in [200, 201]:
        return "✅ সফলভাবে গিটহাবে আপলোড হয়েছে।"
    else:
        return f"❌ আপলোডে সমস্যা হয়েছে: {response.text}"

def git_pull():
    try:
        result = subprocess.run(
            ["git", "pull", "origin", "main"],
            capture_output=True,
            text=True
        )
        if "Already up to date." in result.stdout:
            return "কোন আপডেট নেই।"
        else:
            return "নতুন আপডেট পেয়েছে।"
    except Exception as e:
        return f"গিট পুলে সমস্যা: {e}"
