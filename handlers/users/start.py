import sqlite3
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, db, bot
from data.config import ADMINS
from keyboards.default.menuKeyboard import Menu




@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    id = message.from_user.id
    name = message.from_user.full_name
    username = message.from_user.username
    # Foydalanuvchini bazaga qo'shamiz
    if username:
        try:
            db.add_user(id=id, name=name, email=username)
        except sqlite3.IntegrityError as err:
            pass
    else:
        try:
            db.add_user(id=id, name=name)
        except sqlite3.IntegrityError as err:
            pass
    xabar=f"Assalomu Alaykum. <b>{name}.</b>\nXush Kelibsiz! 😊"
    await message.answer(xabar,reply_markup=Menu)
    # Adminga xabar beramiz
    count = db.count_users()[0]
    msg  = f"<b>Boshliq botga odam qo'shildi</b>\n\n"
    msg += f"<b>@{username}</b>\n "
    msg += f"<b>{name}</b>\n"
    msg += f" <b>{id}</b>\n\n"
    msg += f"Bazada <b>{count}</b> ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg ,reply_markup=Menu)
    # await message.answer_audio(f"https://cdn.islamic.network/quran/audio-surah/128/ar.alafasy/{k}.mp3")
    await state.finish()














