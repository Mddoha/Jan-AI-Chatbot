import json

def load_config(path='config.json'):
    """
    config.json ফাইল থেকে সেটিংস লোড করে dict আকারে রিটার্ন করে
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        print(f"Error: Configuration file {path} পাওয়া যায়নি।")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Configuration ফাইলটি সঠিক JSON ফরম্যাটে নেই।")
        return {}
