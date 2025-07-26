import logging

# লগ ফাইলের নাম এবং সেটিংস
logging.basicConfig(
    filename='logs/bot_logs.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)
