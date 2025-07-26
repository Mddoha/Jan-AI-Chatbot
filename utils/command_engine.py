def process_command(text, user_id, large=False):
    """
    টেক্সট কমান্ড প্রসেস করে রেসপন্স তৈরি করে।
    বড় কমান্ড হলে ভিন্নভাবে হ্যান্ডেল করে।
    """

    # ✅ Command prefix বাদ দাও
    command = text.replace("হানি", "").strip()

    if large:
        # বড় কমান্ড হলে বিশেষ প্রসেসিং (উদাহরণস্বরূপ)
        return f"🔎 আপনার বড় কমান্ডটি বিশ্লেষণ করা হচ্ছে...\n\n👉 `{command}`"
    else:
        # সাধারণ কমান্ড
        return f"🤖 আপনি বলেছেন: `{command}`"
