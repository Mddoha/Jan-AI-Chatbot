def process_command(text, user_id, large=False):
    """
    টেক্সটকে প্রসেস করে বুঝবে কী করতে হবে।
    বড় কমান্ড হলে মাল্টি লাইন টাস্ক হ্যান্ডেল করে,
    ছোট হলে সরাসরি রিপ্লাই।
    """

    command = text.replace("হানি", "").replace("✅", "").strip()

    if not command:
        return "🥲 কোনো নির্দেশনা দেননি..."

    # উদাহরণ হিসেবে কিছু কাস্টম কমান্ড
    if "github" in command.lower():
        return "GitHub সম্পর্কিত কমান্ড প্রসেস হচ্ছে..."
    elif "blog" in command.lower():
        return "Blogger সম্পর্কিত কমান্ড চালু হচ্ছে..."
    elif "তুমি কে" in command.lower():
        return "আমি Jan-AI-Chatbot, আপনার নিজস্ব AI সহকারী 🤖"
    else:
        if large:
            return f"বড় কমান্ড বিশ্লেষণ করা হলো:\n\n{command}"
        else:
            return f"আপনার কমান্ড ছিল: {command}"
