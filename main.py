from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handlers import handle_message

def start(update, context):
    user = update.effective_user
    update.message.reply_text(f"Salom, {user.first_name}! Assalomu alaykum! Men suhbat botiman 😊")

def main():
    updater = Updater("7752581705:AAGMWx2IkpqCb13pKxiJ2pXdi9OS-VWqTE0", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
