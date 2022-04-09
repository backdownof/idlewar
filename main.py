from config import TELE_TOKEN

from telegram.ext import Updater

updater = Updater(token=TELE_TOKEN, use_context=True)