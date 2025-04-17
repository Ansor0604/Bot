import threading
from flask import Flask
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "YOUR_BOT_TOKEN"

def start(update, context):
    update.message.reply_text("Bot ishlayapti!")

def reply_handler(update, context):
    text = update.message.text
    update.message.reply_text(f"Siz yozdingiz: {text}")

# Flask server
app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running!"

def run_flask():
    app.run(host="0.0.0.0", port=8080)

def run_bot():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_handler))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    run_bot()
