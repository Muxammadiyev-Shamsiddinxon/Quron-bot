from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
import requests

sura_va_raqam = CallbackData("sura", "sura_nomi", 'raqam')





#         oraliqlardi bolib chiqayapman
##############################################################################################################
Suralar_oraligi_keyboard = InlineKeyboardMarkup(row_width=2)
lst = ['1-20 📖', '20-40 📖', '40-60 📖', '60-80 📖', '80-100 📖', '100-114 📖']
for oraliq in lst:
    Suralar_oraligi_keyboard.insert(InlineKeyboardButton(text=f"{oraliq}", callback_data=f"{oraliq}"))
##############################################################################################################



###############################################################################################################
# barcha sura nomlarni chaqirib olayapti requests surov yuborish orqali
url=f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/info.json"
r = requests.get(url)
r=r.json()
###############################################################################################################


#                    1 - 20 gacha suralarni keyboard qilib yasab olayapmiz
################################################################################################################
Suralar_keyboard_1_20 = InlineKeyboardMarkup(row_width=2)
for n in range(0,20):
    sura = r['chapters'][n]['name']
    Suralar_keyboard_1_20.insert(InlineKeyboardButton(text=f"{n+1}.    {sura}", callback_data=sura_va_raqam.new(sura_nomi=sura, raqam=n+1)))
Suralar_keyboard_1_20.insert(InlineKeyboardButton(text="20-40 📖", callback_data="20-40 📖"))
################################################################################################################



#                    20 - 40 gacha suralarni keyboard qilib yasab olayapmiz
################################################################################################################
Suralar_keyboard_20_40 = InlineKeyboardMarkup(row_width=2)
for n in range(20,40):
    sura = r['chapters'][n]['name']
    Suralar_keyboard_20_40.insert(InlineKeyboardButton(text=f"{n+1}.    {sura}", callback_data=sura_va_raqam.new(sura_nomi=sura, raqam=n+1)))
Suralar_keyboard_20_40.insert(InlineKeyboardButton(text="1-20 📖", callback_data="1-20 📖"))
Suralar_keyboard_20_40.insert(InlineKeyboardButton(text="40-60 📖", callback_data="40-60 📖"))
################################################################################################################


#                    40 - 60 gacha suralarni keyboard qilib yasab olayapmiz
################################################################################################################
Suralar_keyboard_40_60 = InlineKeyboardMarkup(row_width=2)
for n in range(40,60):
    sura = r['chapters'][n]['name']
    Suralar_keyboard_40_60.insert(InlineKeyboardButton(text=f"{n+1}.    {sura}", callback_data=sura_va_raqam.new(sura_nomi=sura, raqam=n+1)))
Suralar_keyboard_40_60.insert(InlineKeyboardButton(text="20-40 📖", callback_data="20-40 📖"))
Suralar_keyboard_40_60.insert(InlineKeyboardButton(text="60-80 📖", callback_data="60-80 📖"))
################################################################################################################



#                    60 - 80 gacha suralarni keyboard qilib yasab olayapmiz
################################################################################################################
Suralar_keyboard_60_80 = InlineKeyboardMarkup(row_width=2)
for n in range(60,80):
    sura = r['chapters'][n]['name']
    Suralar_keyboard_60_80.insert(InlineKeyboardButton(text=f"{n+1}.    {sura}", callback_data=sura_va_raqam.new(sura_nomi=sura, raqam=n+1)))
Suralar_keyboard_60_80.insert(InlineKeyboardButton(text="40-60 📖", callback_data="40-60 📖"))
Suralar_keyboard_60_80.insert(InlineKeyboardButton(text="80-100 📖", callback_data="80-100 📖"))
################################################################################################################


#                    80 - 100 gacha suralarni keyboard qilib yasab olayapmiz
################################################################################################################
Suralar_keyboard_80_100 = InlineKeyboardMarkup(row_width=2)
for n in range(80,100):
    sura = r['chapters'][n]['name']
    Suralar_keyboard_80_100.insert(InlineKeyboardButton(text=f"{n+1}.    {sura}", callback_data=sura_va_raqam.new(sura_nomi=sura, raqam=n+1)))
Suralar_keyboard_80_100.insert(InlineKeyboardButton(text="60-80 📖", callback_data="60-80 📖"))
Suralar_keyboard_80_100.insert(InlineKeyboardButton(text="100-114 📖", callback_data="100-114 📖"))
################################################################################################################



#                    100 - 114 gacha suralarni keyboard qilib yasab olayapmiz
################################################################################################################
Suralar_keyboard_100_114 = InlineKeyboardMarkup(row_width=2)
for n in range(100,114):
    sura = r['chapters'][n]['name']
    Suralar_keyboard_100_114.insert(InlineKeyboardButton(text=f"{n+1}.    {sura}", callback_data=sura_va_raqam.new(sura_nomi=sura, raqam=n+1)))
Suralar_keyboard_100_114.insert(InlineKeyboardButton(text="80-100 📖", callback_data="80-100 📖"))
################################################################################################################

