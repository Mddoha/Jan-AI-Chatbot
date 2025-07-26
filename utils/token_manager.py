import time

class TokenManager:
    def __init__(self, token, expiry_time=None):
        self.token = token
        self.expiry_time = expiry_time  # Unix timestamp

    def is_token_expired(self):
        if self.expiry_time is None:
            return False
        return time.time() > self.expiry_time

    def update_token(self, new_token, new_expiry_time=None):
        self.token = new_token
        self.expiry_time = new_expiry_time

    def get_token(self):
        if self.is_token_expired():
            # এখানে টোকেন রিফ্রেশ লজিক বসাতে পারো
            print("টোকেন এক্সপায়ার হয়েছে, রিফ্রেশ করা প্রয়োজন।")
        return self.token
