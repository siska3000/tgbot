import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from config import telegram_bot_token

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm Mr.68! How can help you?")


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello!")


async def name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm Mr.68!")


if __name__ == '__main__':
    application = ApplicationBuilder().token(telegram_bot_token).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    start_handler = CommandHandler('hello', hello)
    application.add_handler(start_handler)

    start_handler = CommandHandler('name', name)
    application.add_handler(start_handler)

    application.run_polling()