from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



Admin_panel = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
list2 = ["Obunachilar", "Obunachilar Soni", "Reklama", "Quron bot"]
for key in list2:
    Admin_panel.insert(KeyboardButton(text=key))


Menu_admin = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
list3 = ["📖 Quron", "🕌 Namoz", "📅 Namoz Vaqti", "☪️ 40 Farz", "👮‍♂️Admin Panel"]
for key in list3:
    Menu_admin.insert(KeyboardButton(text=key))


