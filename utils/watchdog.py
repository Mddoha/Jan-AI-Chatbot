import subprocess
import time
import sys
import os
import threading

BOT_SCRIPT = "main.py"  # তোমার বটের মেইন ফাইলের নাম

def start_bot():
    # বটকে সাবপ্রসেস হিসেবে চালাবে
    return subprocess.Popen([sys.executable, BOT_SCRIPT])

def monitor_bot(proc):
    while True:
        # যদি বট প্রোসেস শেষ হয় (ক্র্যাশ/বন্ধ হয়ে যায়), রিস্টার্ট করবে
        if proc.poll() is not None:
            print("বট বন্ধ হয়েছে, পুনরায় চালু করা হচ্ছে...")
            proc = start_bot()
        time.sleep(5)

def main():
    bot_process = start_bot()
    monitor_thread = threading.Thread(target=monitor_bot, args=(bot_process,))
    monitor_thread.daemon = True
    monitor_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("ওয়াচডগ বন্ধ করা হচ্ছে...")
        bot_process.terminate()
        sys.exit(0)

if __name__ == "__main__":
    main()
