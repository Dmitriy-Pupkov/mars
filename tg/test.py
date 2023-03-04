import datetime
import os
import logging
from dotenv import load_dotenv
from telegram.ext import Application
from telegram.ext import CommandHandler

load_dotenv()
token = os.environ.get('TOKEN')
TOKEN = '5923980996:AAF_jL5eHv0gIHC98-_p2LTP-wQ8gzXTPrA'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)


async def time(update, context):
    await update.message.reply_text(f'Текущее время: {datetime.datetime.now().time()}')


async def data(update, context):
    await update.message.reply_text(f'Сегодня: {datetime.datetime.now().date()}')


def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("data", data))
    application.add_handler(CommandHandler("time", time))
    application.run_polling()


if __name__ == 'main':
    main()
