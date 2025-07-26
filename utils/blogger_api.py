import requests
import json
from config import BLOGGER_API_TOKEN, BLOGGER_BLOG_ID

BLOGGER_API_URL = f"https://www.googleapis.com/blogger/v3/blogs/{BLOGGER_BLOG_ID}/posts/"

def create_post(title, content):
    headers = {
        "Authorization": f"Bearer {BLOGGER_API_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "kind": "blogger#post",
        "title": title,
        "content": content
    }
    response = requests.post(BLOGGER_API_URL, headers=headers, data=json.dumps(data))
    if response.status_code == 200 or response.status_code == 201:
        return "✅ ব্লগ পোস্ট সফলভাবে তৈরি হয়েছে।"
    else:
        return f"❌ ব্লগ পোস্ট তৈরিতে সমস্যা: {response.text}"
