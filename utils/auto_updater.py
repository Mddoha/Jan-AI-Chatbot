import subprocess
import time
import sys
import os

# তোমার লোকাল রিপোজিটরি পাথ (প্রয়োজন হলে বদলে নিতে পারো)
LOCAL_REPO_PATH = "./"

# মূল ব্রাঞ্চ (তুমি যদি অন্য ব্রাঞ্চ ব্যবহার করো, সেটিও পরিবর্তন করো)
BRANCH = "main"

def git_pull():
    try:
        result = subprocess.run(
            ["git", "pull", "origin", BRANCH],
            cwd=LOCAL_REPO_PATH,
            capture_output=True,
            text=True,
        )
        if "Already up to date." in result.stdout:
            print("কোন নতুন আপডেট পাওয়া যায়নি।")
            return False
        else:
            print("নতুন আপডেট পাওয়া গেছে, বট রিস্টার্ট হবে।")
            print(result.stdout)
            return True
    except Exception as e:
        print(f"Git pull করতে সমস্যা হয়েছে: {e}")
        return False

def restart_bot():
    print("বট রিস্টার্ট করা হচ্ছে...")
    # নিচের কোড বটকে আবার চালু করবে, তুমি চাইলে নিজস্ব স্টার্টার দিতে পারো
    os.execv(sys.executable, [sys.executable] + sys.argv)

def main():
    while True:
        updated = git_pull()
        if updated:
            restart_bot()
        time.sleep(300)  # ৫ মিনিট অপেক্ষা করবে, তারপর আবার চেক করবে

if __name__ == "__main__":
    main()
