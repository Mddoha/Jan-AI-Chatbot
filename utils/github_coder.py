import requests
import base64
from config import GITHUB_TOKEN, GITHUB_REPO

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def create_or_update_file(path, content, commit_message):
    """
    GitHub-এ নির্দিষ্ট path-এ ফাইল তৈরি বা আপডেট করে।
    """
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{path}"

    # আগের ফাইল আছে কিনা চেক করা
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        sha = response.json()["sha"]
    else:
        sha = None

    encoded_content = base64.b64encode(content.encode()).decode()

    data = {
        "message": commit_message,
        "content": encoded_content,
        "branch": "main"
    }

    if sha:
        data["sha"] = sha  # পুরাতন ফাইল overwrite

    response = requests.put(url, headers=headers, json=data)
    return response.status_code == 201 or response.status_code == 200

def handle_github_command(command_text):
    """
    টেক্সট থেকে কোড বের করে GitHub-এ ফাইল বানায়।
    """
    try:
        lines = command_text.strip().split('\n')
        filename = lines[0].strip()
        code = "\n".join(lines[1:])
        success = create_or_update_file(f"auto/{filename}", code, f"Auto update: {filename}")
        if success:
            return f"✅ `{filename}` ফাইলটি GitHub-এ আপলোড করা হয়েছে!"
        else:
            return "❌ GitHub-এ ফাইল আপলোড ব্যর্থ হয়েছে!"
    except Exception as e:
        return f"⚠️ ত্রুটি: {str(e)}"
