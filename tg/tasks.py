import os
import logging
from dotenv import load_dotenv
from telegram.ext import CommandHandler, Application, MessageHandler, filters, ConversationHandler, CallbackContext
from telegram import ReplyKeyboardMarkup, Update, ReplyKeyboardRemove

load_dotenv()
BOT_TOKEN = os.environ.get('TOKEN')

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

stih = '''Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный -
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела -
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''.split('\n')

WAIT_NEXT_STRING = 1
WAIT_REPEAT_OR_EXIT = 2
ATTEMP_OR_SUPHLER = 3
LAST_INDEX = 'last_index'


def normalize(string):
    return ''.join(''.join(filter(lambda x: x.isalpha() or x.isspace(), string)).strip().split()).lower()


async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('Давайте почитаем стихотворение поочереди. Я начну.')
    await update.message.reply_text(stih[27])
    context.user_data[LAST_INDEX] = 27
    return WAIT_NEXT_STRING


async def stop(update: Update, context: CallbackContext):
    await update.message.reply_text('Всего доброго!')
    return ConversationHandler.END


async def continue_or_break(index, update, context):
    if index > len(stih) - 1:
        await update.message.reply_text('Стихотворение закончилось. Повторим? (/yes /no)')
        return WAIT_REPEAT_OR_EXIT
    elif index == len(stih) - 1:
        await update.message.reply_text(stih[index])
        await update.message.reply_text('Стихотворение закончилось. Повторим? (/yes /no)')
        return WAIT_REPEAT_OR_EXIT
    await update.message.reply_text(stih[index])
    context.user_data[LAST_INDEX] = index
    return WAIT_NEXT_STRING


async def waiting_next_string(update: Update, context: CallbackContext):
    string = update.message.text
    current_index = context.user_data[LAST_INDEX] + 1
    if normalize(string) == normalize(stih[current_index]):
        return await continue_or_break(current_index + 1, update, context)
    else:
        await update.message.reply_text('Нет, не так. Попробуйте ещё раз или используйте подсказку /suphler')
        return ATTEMP_OR_SUPHLER


async def suphler(update: Update, context: CallbackContext):
    return await continue_or_break(context.user_data[LAST_INDEX] + 1, update, context)


def main():
    application = Application.builder().token(BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            WAIT_NEXT_STRING: [MessageHandler(filters.TEXT & ~filters.COMMAND, waiting_next_string)],
            ATTEMP_OR_SUPHLER: [MessageHandler(filters.TEXT & ~filters.COMMAND, waiting_next_string),
                                CommandHandler('suphler', suphler)],
            WAIT_REPEAT_OR_EXIT: [CommandHandler('yes', start), CommandHandler('no', stop)]

        },

        fallbacks=[CommandHandler('stop', stop)]
    )

    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
