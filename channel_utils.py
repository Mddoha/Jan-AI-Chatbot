from config import CHANNEL_USERNAMES, OWNER_UID

def is_authorized_channel(channel_username):
    """
    চ্যানেল যাচাই করে: অনুমোদিত চ্যানেল কিনা
    """
    return channel_username in CHANNEL_USERNAMES

def list_channels(user_id):
    """
    অনুমোদিত ইউজারকে সব চ্যানেলের তালিকা পাঠায়
    """
    if user_id != OWNER_UID:
        return "❌ আপনি এই তথ্য দেখতে পারেন না।"
    
    if not CHANNEL_USERNAMES:
        return "⚠️ কোনো চ্যানেল যুক্ত করা হয়নি।"
    
    msg = "📢 অনুমোদিত চ্যানেল তালিকা:\n\n"
    for ch in CHANNEL_USERNAMES:
        msg += f"🔹 @{ch}\n"
    return msg
