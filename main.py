#!/usr/bin/env python
# coding: utf-8

import os

import signal

import requests

from telegram import Update

from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters


TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
ZAPIER_CALLBACK = os.getenv('ZAPIER_CALLBACK')

updater = Updater(token=TELEGRAM_TOKEN, use_context=True)

dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    text = "I'm a bot, I will forward your messages to the todo list!"

    context.bot.send_message(chat_id=chat_id, text=text)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def todo(update: Update, context: CallbackContext):
    print('processing another message...')

    message = update.message

    print(update.effective_chat)
    print(message)

    chat_id = update.effective_chat.id

    text = message['text']
    dt = message['date']

    if text.startswith('/todo'):
        text = text[len('/todo'):].strip()

    if len(text) == 0:
        print('empty, exiting')
        return

    output = {
        'text': text,
        'date': dt.strftime('%Y-%m-%d')
    }

    requests.post(ZAPIER_CALLBACK, json=output)

    text = "Done! Message saved to the todo list!"
    context.bot.send_message(chat_id=chat_id, text=text)


todo_command_handler = CommandHandler('todo', todo)
dispatcher.add_handler(todo_command_handler)

todo_text_handler = MessageHandler(Filters.text & (~Filters.command), todo)
dispatcher.add_handler(todo_text_handler)


print('starting listening...')
updater.start_polling()

updater.idle([signal.SIGINT])
