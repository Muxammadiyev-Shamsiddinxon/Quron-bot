import asyncio
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ChatMemberUpdated, ReplyKeyboardRemove, InputFile
from data.config import ADMINS
from keyboards.default.admin_keyboard import Admin_panel, Menu_admin
from keyboards.default.menuKeyboard import Menu
from loader import dp, db, bot
from states.reklama_yuborish import State_reklama_yuborish

@dp.message_handler(text="👮‍♂️Admin Panel", state='*', user_id=ADMINS)
@dp.message_handler(text="/start", state='*', user_id=ADMINS)
async def bot_start(message: types.Message, state: FSMContext):
    xabar = f"<b>Quron Tafsiri bot Admin Panel</b> "
    await message.answer(xabar, reply_markup=Admin_panel)
    await state.finish()


@dp.message_handler(text='Quron bot', state='*', user_id=ADMINS)
async def Suralar_oraliq(message: types.Message, state: FSMContext):
    text = "Quron Bot"
    await message.answer(text, reply_markup=Menu_admin)
    await state.finish()


@dp.message_handler(text="🔙 Ortga", state='*', user_id=ADMINS)
@dp.message_handler(text="Imlo va Kurs", user_id=ADMINS)
async def Imlo_Kurs(message: types.Message, state: FSMContext):
    xabar = f"<b>Imlo va Kurs bot</b> "
    await message.answer(xabar, reply_markup=Menu_admin)
    await state.finish()



@dp.message_handler(text="Obunachilar Soni", user_id=ADMINS)
async def obunachilar_soni(message: types.Message):
    users = db.select_all_users()
    x=f"<b>{len(users)}</b> - ta"
    await message.answer(x)



@dp.message_handler(text="Obunachilar", user_id=ADMINS)
async def obunachilar(message: types.Message):
    users = db.select_all_users()
    n = 1
    for user in users:
        if user[2]:
            x = f"\n<b>{n}.</b> id__  <b>{user[0]}</b>\n"
            x+= f"ism__  <b>{user[1]}</b>\n"
            x += f"username__  @{user[2]}"
            n += 1
            await message.answer(x)
            await asyncio.sleep(0.1)
        else:
            x = f"\n<b>{n}.</b> id__  <b>{user[0]}</b>\n"
            x += f"ism__  <b>{user[1]}</b>\n"
            n += 1
            await message.answer(x)
            await asyncio.sleep(0.1)



# state buyicha qilingan
#======================reklama==================================================================================
@dp.message_handler(text="Reklama", user_id=ADMINS)
async def send_reklama(message: types.Message):
    text = f"Reklamani yuboring !\n"
    text += f"U video, rasm, audio, ixtiyoriy bo'lishi mumkin !"
    await message.answer(f"<b>{text}</b>", reply_markup=ReplyKeyboardRemove())
    await State_reklama_yuborish.reklama.set()


@dp.message_handler(state = State_reklama_yuborish.reklama, content_types=types.ContentType.ANY, user_id=ADMINS)
async def send_reklama(message: types.Message, state: FSMContext):
    users = db.select_all_users()
    bordi = 0
    bormadi = 0
    for user in users:
        try:
            user_id = user[0]
            xabar = f"<b>✅Reklama yuborildi</b>  {user_id}"
            # bu 1-usul siz yuborgan xabarni copy qilib foydalanuvchiga yuboradi
            # await bot.copy_message(chat_id=user_id, from_chat_id=message.from_user.id, message_id=message.message_id)
            # bu 2-usul siz yuborgan xabarni copy qilib foydalanuvchiga yuboradi
            await message.send_copy(chat_id=user_id, reply_markup=Menu)
            await message.answer(text=xabar)
            bordi+=1
            await asyncio.sleep(0.1)
        except:
            user_id = user[0]
            xabar = f"<b>❌Reklama yuborilmadi</b>  {user_id}"
            await message.answer(text=xabar)
            bormadi+=1
            await asyncio.sleep(0.1)
    soni = f"{bordi}-ta Yuborildi✅\n{bormadi}-ta Yuborilmadi❌"
    await message.answer(f"<b>{soni}</b>")
    await state.finish()
#==========================================================================================================





# botdan chiqgan yoki kirganini bilib turadi
@dp.my_chat_member_handler()
async def some_handler(chat_member: ChatMemberUpdated):
    text = f"id: {chat_member.chat.id}\nism: {chat_member.from_user.full_name}\n"
    text += f"oldingi_status: {chat_member.old_chat_member.status}\n"
    text += f"hozirgi_status: {chat_member.new_chat_member.status}"
    await bot.send_message(chat_id=ADMINS, text=text)



