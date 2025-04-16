import json
import os
from datetime import datetime

FILE_PATH = "users.json"

def load_users():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}

def save_users(data):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def register_user(user, user_data):
    user_id = str(user.id)
    if not isinstance(user_data.get(user_id), dict):
        user_data[user_id] = {
            "ism": user.first_name,
            "username": user.username or "yo‘q",
            "til": user.language_code,
            "royxat_vaqti": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        save_users(user_data)

