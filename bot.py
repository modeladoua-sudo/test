import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# Перевірка токена
TOKEN = os.environ.get("BOT_TOKEN")
print("TOKEN VALUE:", TOKEN)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        await update.message.reply_text(
            f"Я бачу текст:\n{update.message.text}"
        )

if TOKEN is None:
    raise ValueError("BOT_TOKEN is NOT set in environment variables!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

app.run_polling()
