import yaml
import logging

from asyncore import dispatcher
from telegram.ext import Updater
from context import start_handler, echo_handler, unknown_handler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def init():
    global bot_token

    with open('./config.yaml') as f:

        try: 
            docs = yaml.load_all(f, Loader=yaml.FullLoader)

            for doc in docs:
                for k, v in doc.items():
                    if k == 'bot_token':
                        bot_token = v
        except yaml.YAMLError as exc:
            logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.ERROR)

init()

updater = Updater(token=bot_token)
dispatcher = updater.dispatcher


dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(unknown_handler)


updater.start_polling()

