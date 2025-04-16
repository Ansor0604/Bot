from utils import load_users, save_users, register_user

user_data = load_users()

def handle_message(update, context):
    user = update.effective_user
    user_id = str(user.id)
    user_input = update.message.text.lower()

    register_user(user, user_data)  # ⬅️ Yangi foydalanuvchini ro'yxatdan o'tkaz

    name = user_data[user_id]["ism"]

    if "salom" in user_input:
        response = f"Va alaykum assalom, {name}!"
    elif "qalesan" in user_input:
        response = f"Alhamdulillah yaxshi, {name}. Sizchi?"
    elif "rahmat" in user_input:
        response = "Doimo xizmatda!"
    elif "isming nima" in user_input:
        response = "Mening ismim Forever"
    else:
        response = f"Kechirasiz, {name}. Bu haqida hali bilmayman."

    update.message.reply_text(response)
