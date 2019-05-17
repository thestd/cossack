# -*-codding: utf-8-*-

from src.dispatcher import updater


def run():
    updater.start_polling()
    updater.idle()
