import threading
from flask import Flask
from telegram import Bot
from telegram.ext import Updater, CommandHandler

TOKEN = "7752581705:AAGMWx2IkpqCb13pKxiJ2pXdi9OS-VWqTE0"  # <-- O'z tokeningizni yozing

# Telegram Bot funksiyasi
def start(update, context):
    update.message.reply_text("Bot ishlayapti!")

# Flask serveri - Render Web Service uchun
app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running!"

# Flaskni alohida ipda ishga tushirish
def run_flask():
    app.run(host="0.0.0.0", port=8080)

# Botni ishga tushirish
def run_bot():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

# Har ikkala xizmatni parallel ishga tushiramiz
if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    run_bot()
