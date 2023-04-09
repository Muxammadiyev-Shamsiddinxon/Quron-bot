from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

sura_va_raqam = CallbackData("sura", "sura_nomi", 'raqam')



lst = ['⬅️', '➡️']

################################################################################################################
Oyat_oraliq = InlineKeyboardMarkup(row_width=2)
for n in lst:
    Oyat_oraliq.insert(InlineKeyboardButton(text=f"{n}", callback_data=f"{n}"))

################################################################################################################


################################################################################################################
Oyat_boshi= InlineKeyboardMarkup(row_width=1)
Oyat_boshi.insert(InlineKeyboardButton(text='➡️', callback_data='➡️'))
################################################################################################################

################################################################################################################
Oyat_oxiri= InlineKeyboardMarkup(row_width=1)
Oyat_oxiri.insert(InlineKeyboardButton(text='⬅️', callback_data='⬅️'))
################################################################################################################
