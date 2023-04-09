from aiogram.types import  ReplyKeyboardMarkup ,  KeyboardButton





#         Namozlar nafl va jamoat
##############################################################################################################
Nafl_jamoat = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
lst = ["🕌 Nafl namozlar", "👥 Juma", "☪️ Qurbon hayiti", "☪️ Ramazon hayiti", "🌆 Janoza", "🔙 Ortga", "🏠 Menu"]
for key in lst:
    Nafl_jamoat.insert(KeyboardButton(text=key))
##############################################################################################################
