from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp



@dp.message_handler(CommandHelp(), state='*')
async def bot_help(message: types.Message, state: FSMContext):
    text="Botdan foydalanish uchun /start tugmasini bosing."
    await message.answer(text)
    await state.finish()

