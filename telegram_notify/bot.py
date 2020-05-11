import requests
from decouple import config, Csv

import logging
logger = logging.getLogger(__name__)

BOT_URL = config("BOT_URL", default="https://api.telegram.org")
BOT_TOKEN = config('BOT_TOKEN', default="")
BOT_CHATIDS = config('BOT_CHATIDS', cast=Csv(), default="")


def api_url(command):
    return "{}/bot{}/{}".format(BOT_URL, BOT_TOKEN, command)


def send_message(message):
    if not BOT_URL or not BOT_TOKEN or not BOT_CHATIDS:
        return
    url = api_url("sendMessage")
    for chat_id in BOT_CHATIDS:
        json_data = {"chat_id": chat_id, "text": message, "parse_mode": 'HTML'}
        requests.post(url, json=json_data)


def send_document(message, filename):
    if not BOT_URL or not BOT_TOKEN or not BOT_CHATIDS:
        return
    url = api_url("sendDocument")
    files = {'document': open(filename, "rb")}
    for chat_id in BOT_CHATIDS:
        json_data = {"chat_id": chat_id, "caption": message, "parse_mode": 'HTML'}
        requests.post(url, data=json_data, files=files)


def send_test_message():
    send_message("Sending direct message ☺ ")
    logger.debug("Sending logger.debug")
    logger.info("Sending logger.info")
    logger.warning("Sending logger.warning")
    logger.error("Sending logger.error")
    # send_document("hello world", "/tmp/filename.txt")
