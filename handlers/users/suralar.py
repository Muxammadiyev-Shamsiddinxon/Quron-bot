from aiogram import types
from aiogram.dispatcher import FSMContext
import os
from loader import dp
from handlers.namoz_api import namoz
from aiogram.types import CallbackQuery, InputFile
from keyboards.default.menuKeyboard import Menu
from keyboards.default.nafl_jamoat import Nafl_jamoat
from keyboards.default.namozlar_keyboard import Namoz_keyboard
from keyboards.inline.suralar_oraligi_keyboard import(
    Suralar_oraligi_keyboard,
    Suralar_keyboard_1_20,
    Suralar_keyboard_20_40,
    Suralar_keyboard_40_60,
    Suralar_keyboard_60_80 ,
    Suralar_keyboard_80_100,
    Suralar_keyboard_100_114,
)


# @dp.message_handler(content_types=types.ContentType.ANY, state="*")
# async def videolar(message: types.Message, state: FSMContext):
#     id = message.photo[-1].file_id
#     await message.answer(id)
#     await state.finish()



########################################################################################################################
@dp.message_handler(text="🏠 Menu", state='*')
async def Namozlar(message: types.Message, state: FSMContext):
    text = "🏠 Menu"
    await message.answer(text, reply_markup=Menu)
    await state.finish()
########################################################################################################################

########################################################################################################################
@dp.message_handler(text="🔙 Ortga", state='*')
async def Namozlar(message: types.Message, state: FSMContext):
    text = "🕌 Namozlar"
    await message.answer(text, reply_markup=Namoz_keyboard)
    await state.finish()
########################################################################################################################


#########################     Namozlar   ###############################################################################
########################################################################################################################
@dp.message_handler(text="🕌 Namoz", state='*')
async def Namozlar(message: types.Message, state: FSMContext):
    text = "🕌 Namozlar"
    await message.answer(text, reply_markup=Namoz_keyboard)
    await state.finish()
########################################################################################################################
########################################################################################################################




#########################     Azon va Duosi   ##########################################################################
########################################################################################################################
@dp.message_handler(text="Azon va Duosi")
async def Azon_umumiy(message: types.Message):
    album = types.MediaGroup()
    azon_audio = "CQACAgIAAxkBAAIV6GPoVEY_LLiq56LfPmaICCR-N40XAAJHJQACJ7pASxSP8BrZkxz9LgQ"
    azon_text = "AgACAgIAAxkBAAIWGWPoWUod-VIspSsyLonhIem7OS0LAALxxDEbVhFJSwUNXIXuBgRuAQADAgADeQADLgQ"
    azon_duo = "AgACAgIAAxkBAAIWF2PoWTSJKMjj-ePC5I5OcjiODb6jAALwxDEbVhFJS1gsduVUzLjSAQADAgADeQADLgQ"
    text = "Azon:   Text, Duo\n\n@IslomQuron_bot"
    album.attach_photo(photo=azon_text)
    album.attach_photo(photo=azon_duo, caption=text)
    await message.answer_audio(azon_audio, caption="Mishari Rashid Azan")
    await message.answer_media_group(media=album)
########################################################################################################################
########################################################################################################################




#########################     Bomdod   #################################################################################
########################################################################################################################
@dp.message_handler(text="🌄 Bomdod")
async def Bomdod(message: types.Message):
    video_id_erkaklar = "BAACAgIAAxkBAAIVRGPoQLaX54crniytiLUcr7jQkIitAAJgEwACgnCJSijrB-uCr6IILgQ"
    video_id_ayollar = "BAACAgIAAxkBAAIVRmPoQMLfmCmqSCDBektHyg28ncRmAALXGAACwQw5Sj22IUIwpV0DLgQ"
    text1 = "🌄 Bomdod namozi Erkaklar uchun ✅\n\n@IslomQuron_bot"
    text2 = "🌄 Bomdod namozi Ayollar uchun ✅\n\n@IslomQuron_bot"
    await message.answer_video(video_id_erkaklar, caption=text1)
    await message.answer_video(video_id_ayollar, caption=text2)
########################################################################################################################
########################################################################################################################



#########################     Peshin   #################################################################################
########################################################################################################################
@dp.message_handler(text="🌅 Peshin")
async def Peshin(message: types.Message):
    video_id_erkaklar = "BAACAgIAAxkBAAIVTGPoQvmf8ByWVKCsa2awJ4SGKJL1AAL9FgACVDSwSoB3jSQmQSl0LgQ"
    video_id_ayollar = "BAACAgIAAxkBAAIVTmPoQzLTSPkJRBPlste_Dpe3GSCOAAI0GAACGHQIS8Jm7a1VzsEdLgQ"
    text1 = "🌅 Peshin namozi Erkaklar uchun ✅\n\n@IslomQuron_bot"
    text2 = "🌅 Peshin namozi Ayollar uchun ✅\n\n@IslomQuron_bot"
    await message.answer_video(video_id_erkaklar, caption=text1)
    await message.answer_video(video_id_ayollar, caption=text2)
########################################################################################################################
########################################################################################################################



#########################     Asr      #################################################################################
########################################################################################################################
@dp.message_handler(text="🏞 Asr")
async def Asr(message: types.Message):
    video_id_erkaklar = "BAACAgIAAxkBAAIVUGPoQ81ceUO5gC0U9YCQrOEh8rKIAAKdFAACWwmZSmmRnwm60bH0LgQ"
    video_id_ayollar = "BAACAgIAAxkBAAIVUmPoQ9hlEtsQF0s_odm3KnF9tW3DAALfKAACjDcBSBTUl-3tdvlHLgQ"
    text1 = "🏞 Asr namozi Erkaklar uchun ✅\n\n@IslomQuron_bot"
    text2 = "🏞 Asr namozi Ayollar uchun ✅\n\n@IslomQuron_bot"
    await message.answer_video(video_id_erkaklar, caption=text1)
    await message.answer_video(video_id_ayollar, caption=text2)
########################################################################################################################
########################################################################################################################



#########################     Shom     #################################################################################
########################################################################################################################
@dp.message_handler(text="🏙 Shom")
async def Asr(message: types.Message):
    video_id_erkaklar = "BAACAgIAAxkBAAIVVGPoRImA893UzCsRCa1VkSv0pf8sAAI6EQACF0BpSkmBhcYxo3afLgQ"
    video_id_ayollar = "BAACAgIAAxkBAAIVVmPoRJgMiQEiQiyj8y8Ic7el0DteAAL9EQACl_2ISc8bWa5VqLmALgQ"
    text1 = "🏙 Shom namozi Erkaklar uchun ✅\n\n@IslomQuron_bot"
    text2 = "🏙 Shom namozi Ayollar uchun ✅\n\n@IslomQuron_bot"
    await message.answer_video(video_id_erkaklar, caption=text1)
    await message.answer_video(video_id_ayollar, caption=text2)
########################################################################################################################
########################################################################################################################


#########################     Xufton   #################################################################################
########################################################################################################################
@dp.message_handler(text="🌃 Xufton")
async def Xufton(message: types.Message):
    video_id_erkaklar = "BAACAgIAAxkBAAIVWGPoRVBbc7lRduGE2gqQ4wfRX9rRAAJZFgAC7zgQSrZxC6ky_YS8LgQ"
    video_id_ayollar = "BAACAgIAAxkBAAIVWmPoRVt_chni_THfxeIwegN6gIneAAK4FAACDesIS6lfjXLgGNsuLgQ"
    text1 = "🌃 Xufton namozi Erkaklar uchun ✅\n\n@IslomQuron_bot"
    text2 = "🌃 Xufton namozi Ayollar uchun ✅\n\n@IslomQuron_bot"
    await message.answer_video(video_id_erkaklar, caption=text1)
    await message.answer_video(video_id_ayollar, caption=text2)
########################################################################################################################
########################################################################################################################




#########################     🕌 Nafl va Jamoat  #######################################################################
########################################################################################################################
@dp.message_handler(text="🕌 Nafl va Jamoat")
async def jamoat(message: types.Message):
    text = "🕌 Nafl va Jamoat namozlari "
    await message.answer(text, reply_markup=Nafl_jamoat)
########################################################################################################################
########################################################################################################################




#########################     Nafl namozlar     ########################################################################
########################################################################################################################
@dp.message_handler(text="🕌 Nafl namozlar")
async def Nafl(message: types.Message):
    Shayx_hazratlari = "BAACAgIAAxkBAAIVXmPoSXpbkTHsEz3UlimIZwrkY4RbAAIGLwACTm5BS-uS9VGl6toHLgQ"
    text = "Nafl namozlari haqida✅\nShayx Hazratlari\n\n@IslomQuron_bot"
    file_id = "BQACAgIAAxkBAAIW52PoabR5536vXlQFflc6SYlRN1k4AAJ7IQACVhFJS5vCNBDlFYVbLgQ"
    await message.answer_document(file_id, caption="Shayx Hazratlari")
    await message.answer_video(Shayx_hazratlari, caption=text)
########################################################################################################################
########################################################################################################################




#########################     Juma namozi       ########################################################################
########################################################################################################################
@dp.message_handler(text="👥 Juma")
async def Juma(message: types.Message):
    Juma = "BAACAgIAAxkBAAIXDmPoa5Zm_rRM7St3L4Bc_b3aeRAVAAJjEwACBr7ASs70z4EwrYf8LgQ"
    text = "Juma namozi haqida✅\n\n@IslomQuron_bot"
    await message.answer_video(Juma, caption=text)
########################################################################################################################
########################################################################################################################




#########################     Qurbon namozi       ######################################################################
########################################################################################################################
@dp.message_handler(text="☪️ Qurbon hayiti")
async def Qurbon(message: types.Message):
    Qurbon = "BAACAgIAAxkBAAIXEmPobbZZKGB2UV_BobCNoYrsxblOAAKMGgACo9tZS1MT1rp8JOv3LgQ"
    text = "Qurbon hayiti namozi haqida✅\n\n@IslomQuron_bot"
    await message.answer_video(Qurbon, caption=text)
########################################################################################################################
########################################################################################################################




#########################     Qurbon namozi       ######################################################################
########################################################################################################################
@dp.message_handler(text="☪️ Ramazon hayiti")
async def Qurbon(message: types.Message):
    Ramazon = "BAACAgIAAxkBAAIXFGPobntCq5BPX4-213v0z1Niwm6UAAItFQACVMZhSveeDthlan4jLgQ"
    text = "Ramazon hayiti namozi haqida✅\n\n@IslomQuron_bot"
    await message.answer_video(Ramazon, caption=text)
########################################################################################################################
########################################################################################################################



#########################     👥 Janoza namozi       ###################################################################
########################################################################################################################
@dp.message_handler(text="🌆 Janoza")
async def Qurbon(message: types.Message):
    Janoza = "BAACAgIAAxkBAAIXFmPob83cZtmAd0w3rH1Tjft-yN7ZAAK1EQACz2T4SgkSanlzKLjzLgQ"
    text = "Janoza namozi haqida \n\n@IslomQuron_bot"
    await message.answer_video(Janoza, caption=text)
########################################################################################################################
########################################################################################################################




###############################  Roza taqvim ###########################################################################
########################################################################################################################
@dp.message_handler(text="⏱ Ro'za Taqvim", state='*')
async def Roza_taqvim(message: types.Message, state: FSMContext):
    photo_id = "AgACAgIAAxkBAAIpZWQa7B5B_XyD5N-rkK5Y31FYKed_AAJVxDEbTr_ZSP1-5wcRSeBuAQADAgADeQADLwQ"
    caption = "⚡️⏱ #ТАҚВИМ\n"
    caption += "Раҳмат ойи - Рамазон муборак!\n\n"
    caption += "☪️ Саҳарлик дуоси:\nНавайту ан асума совма шаҳри рамазона минал фажри илал мағриби, холисан лиллаҳи таъала Аллоҳу акбар.\n\n"
    caption += "☪️ Ифторлик дуоси:\nАллоҳумма лака сумту ва бика аманту ва ъалайка таваккалту ва ъала ризқика афтарту, фағфирли йа ғоффару ма қоддамту ва ма аххорту.\n\n"
    caption += "@IslomQuron_bot"
    await message.answer_photo(photo_id, caption)
    await state.finish()
########################################################################################################################
########################################################################################################################




###############################  40 farz    ############################################################################
########################################################################################################################
@dp.message_handler(text="☪️ 40 Farz", state='*')
async def Qirq_farz(message: types.Message, state: FSMContext):
    photo_id = "AgACAgIAAxkBAAIVJWPoM0yqlfHwF2q2R4QiGgR0Xga9AAJeyDEbG7xBS_92fqnKcSDlAQADAgADeQADLgQ"
    await message.answer_photo(photo_id, caption="Islom Dinining 40 Farzi ✅\n\n@IslomQuron_bot")
    await state.finish()
########################################################################################################################
########################################################################################################################



############################# Namoz vaqtlari ###########################################################################
########################################################################################################################
@dp.message_handler(text='📅 Namoz Vaqti', state='*')
async def Namoz_vaqtlari(message: types.Message, state: FSMContext):
    emoj = await message.answer("⏳")
    id = message.from_user.id
    namoz(id)
    caption = "Namoz Vaqtlari.\n\n@IslomQuron_bot"
    rasm = InputFile(path_or_bytesio=f"rasmlar/{id}.png")
    await emoj.delete()
    await message.answer_photo(rasm, caption=caption, reply_markup=Menu)
    os.remove(f"rasmlar/{id}.png")
    await state.finish()
########################################################################################################################
########################################################################################################################



############################### QURON  #################################################################################
########################################################################################################################
@dp.message_handler(text='📖 Quron', state='*')
async def Suralar_oraliq(message: types.Message, state: FSMContext):
    fotoshayx = InputFile(path_or_bytesio="rasmlar/shayx.jpg")
    #  caption yozib olayapmiz
    caption = f"Shayx Muhammad Sodiq Muhammad Yusuf\nQuron Tafsiri Hilol 📖 \n"
    caption += f"Suralarni Tanlang 📖 ✅"
    await message.answer_photo(photo=fotoshayx, caption=caption, reply_markup=Suralar_oraligi_keyboard)
    await state.finish()
########################################################################################################################
########################################################################################################################






#############################  Bu suarlara      ########################################################################
########################################################################################################################
@dp.callback_query_handler(text="1-20 📖")
async def Suralar20(call: CallbackQuery):
    text = f"1-20 Surani Tanlang 📖 ✅"
    await call.message.edit_caption(caption=text, reply_markup=Suralar_keyboard_1_20)
    



@dp.callback_query_handler(text="20-40 📖")
async def Suralar40(call: CallbackQuery):
    text = f"20-40 Surani Tanlang 📖 ✅"
    await call.message.edit_caption(caption=text, reply_markup=Suralar_keyboard_20_40)
    



@dp.callback_query_handler(text="40-60 📖")
async def Suralar60(call: CallbackQuery):
    text = f"40-60 Surani Tanlang 📖 ✅"
    await call.message.edit_caption(caption=text, reply_markup=Suralar_keyboard_40_60)
    



@dp.callback_query_handler(text="60-80 📖")
async def Suralar80(call: CallbackQuery):
    text = f"60-80 Surani Tanlang 📖 ✅"
    await call.message.edit_caption(caption=text, reply_markup=Suralar_keyboard_60_80)
    



@dp.callback_query_handler(text="80-100 📖")
async def Suralar100(call: CallbackQuery):
    text = f"80-100 Surani Tanlang 📖 ✅"
    await call.message.edit_caption(caption=text, reply_markup=Suralar_keyboard_80_100)
    



@dp.callback_query_handler(text="100-114 📖")
async def Suralar114(call: CallbackQuery):
    text = f"100-114 Surani Tanlang 📖 ✅"
    await call.message.edit_caption(caption=text, reply_markup=Suralar_keyboard_100_114)
    

