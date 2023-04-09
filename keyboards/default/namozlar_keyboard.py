from aiogram.types import  ReplyKeyboardMarkup ,  KeyboardButton





#         Namozlar
##############################################################################################################
Namoz_keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
lst = ["Azon va Duosi", "🌄 Bomdod", "🌅 Peshin", "🏞 Asr", "🏙 Shom", "🌃 Xufton", "🕌 Nafl va Jamoat", "🏠 Menu"]
for key in lst:
    Namoz_keyboard.insert(KeyboardButton(text=key))
##############################################################################################################
