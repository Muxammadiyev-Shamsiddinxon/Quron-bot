from aiogram.types import  ReplyKeyboardMarkup ,  KeyboardButton


Menu = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
list2 = ["📖 Quron", "🕌 Namoz", "📅 Namoz Vaqti", "⏱ Ro'za Taqvim", "☪️ 40 Farz"]
for key in list2:
    Menu.insert(KeyboardButton(text=key))

