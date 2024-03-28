import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

TG_TOKEN = os.getenv('telegram_bot_token')


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name} welcome to transilvanya')


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text.lower()
    if "привіт" in message:
        await update.message.reply_text(f"так")
    else:
        await update.message.reply_text(f"арсен")


app = ApplicationBuilder().token(TG_TOKEN).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
app.run_polling()