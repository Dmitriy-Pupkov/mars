import os
import logging
from dotenv import load_dotenv
from telegram.ext import CommandHandler, Application, MessageHandler, filters, ConversationHandler, CallbackContext
from telegram import ReplyKeyboardMarkup, Update, ReplyKeyboardRemove

load_dotenv()
token = os.environ.get('TOKEN')
BOT_TOKEN = os.environ.get('TOKEN')

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)


async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('Бот может показать вам виртуальную '
                                    'экскурсию по музею. /enter , чтобы войти в музей')


async def enter(update: Update, context: CallbackContext):
    await update.message.reply_text('Добро пожаловать! Пожалуйста, сдайте верхнюю одежду в гардероб!')
    return await to_1(update, context)


async def to_exit(update: Update, context: CallbackContext):
    await update.message.reply_text('Всего доброго, не забудьте забрать верхнюю одежду в гардеробе!',
                                    reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


async def to_1(update: Update, context: CallbackContext):
    await update.message.reply_text('Вы находитесь в зале № 1. Здесь представлено чучело древнего человека',
                                    reply_markup=ReplyKeyboardMarkup([['/to2', '/exit']]))
    return 1


async def to_2(update: Update, context: CallbackContext):
    await update.message.reply_text('Вы находитесь в зале № 2. Здесь представлен скелет динозавра',
                                    reply_markup=ReplyKeyboardMarkup([['/to3']]))
    return 2


async def to_3(update: Update, context: CallbackContext):
    await update.message.reply_text('Вы находитесь в зале № 3. Здесь представлен древний мерседес времён динозавров',
                                    reply_markup=ReplyKeyboardMarkup([['/to1', '/to4']]))
    return 3


async def to_4(update: Update, context: CallbackContext):
    await update.message.reply_text(
        'Вы находитесь в зале № 4. Здесь представлено чучело древнего баяна и сказителя Филлипина Киркоровского',
        reply_markup=ReplyKeyboardMarkup([['/to1']]))
    return 4


def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('enter', enter)],

        states={
            1: [CommandHandler('exit', to_exit), CommandHandler('to2', to_2)],
            2: [CommandHandler('to3', to_3)],
            3: [CommandHandler('to1', to_1), CommandHandler('to4', to_4)],
            4: [CommandHandler('to1', to_1)]
        },

        fallbacks=[]
    )

    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
