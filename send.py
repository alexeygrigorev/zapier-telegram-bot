import os
import sys
import json

from datetime import datetime

import requests
from telegram import Bot

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
ZAPIER_CALLBACK = os.getenv('ZAPIER_CALLBACK')
JSON_MESSAGE_FILE = os.getenv('JSON_MESSAGE_FILE', 'messages.json')

message_id = sys.argv[1]


current_dir = os.path.dirname(os.path.abspath(__file__))

with open(f'{current_dir}/{JSON_MESSAGE_FILE}') as f_in:
    messages = json.load(f_in)

if message_id not in messages:
    raise Exception(f'{message_id} not found in f{JSON_MESSAGE_FILE}')

message_info = messages[message_id]
chat_id = message_info['chat_id']
message = message_info['message']


bot = Bot(token=TELEGRAM_TOKEN)
bot.send_message(chat_id=chat_id, text=message)


now = datetime.now()

zapier_payload = {
    'text': message,
    'date': now.strftime('%Y-%m-%d')
}

requests.post(ZAPIER_CALLBACK, json=zapier_payload)

