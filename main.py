from asyncore import dispatcher
from config import TELE_TOKEN

from telegram.ext import Updater

from context import start_handler, echo_handler, unknown_handler

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


updater = Updater(token=TELE_TOKEN)
dispatcher = updater.dispatcher


dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(unknown_handler)


updater.start_polling()
