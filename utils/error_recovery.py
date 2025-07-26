import traceback

def safe_execute(func, *args, **kwargs):
    """
    যেকোনো ফাংশন নিরাপদে চালানোর জন্য — ত্রুটি হলে ধরবে এবং রিপ্লাই দেবে।
    """
    try:
        return func(*args, **kwargs)
    except Exception as e:
        error_msg = f"⚠️ একটি ত্রুটি ঘটেছে:\n\n{str(e)}\n\n```{traceback.format_exc()}```"
        return error_msg
