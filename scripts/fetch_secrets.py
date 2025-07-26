# scripts/fetch_secrets.py

import os
import requests

# Load GitHub Token from Actions Secret
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
REPO = "Mddoha/Jan-AI-Secrets"
FILES = ["telegram_token.txt", "github_token.txt", "google_client_id.txt"]
BRANCH = "main"

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3.raw"
}

os.makedirs("secrets", exist_ok=True)

for file_name in FILES:
    url = f"https://api.github.com/repos/{REPO}/contents/{file_name}?ref={BRANCH}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(f"secrets/{file_name}", "wb") as f:
            f.write(response.content)
        print(f"✅ Downloaded {file_name}")
    else:
        print(f"❌ Failed to fetch {file_name}: {response.status_code}")
