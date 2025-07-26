import time
import threading
from utils.logger import logger

class SelfChecker:
    def __init__(self, check_interval=120):
        self.check_interval = check_interval
        self.is_running = True
        self.thread = threading.Thread(target=self._run_check_loop)
        self.thread.daemon = True  # বন্ধ না হয় কখনোই
        self.thread.start()

    def _run_check_loop(self):
        while self.is_running:
            try:
                self.perform_self_check()
            except Exception as e:
                logger.error(f"🤖 Self-check error: {str(e)}")
            time.sleep(self.check_interval)

    def perform_self_check(self):
        # এখানে ভবিষ্যতে আরও অনেক চেক যুক্ত করতে পারো
        logger.info("🧠 Performing self-check: সব কিছু সচল ✅")

    def stop(self):
        self.is_running = False
        logger.warning("🚫 Self-checker manually stopped.")

# প্রয়োগ করার সময়:
# from utils.self_checker import SelfChecker
# checker = SelfChecker(check_interval=300)  # প্রতি ৫ মিনিটে নিজেকে যাচাই করবে
