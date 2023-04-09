import time

from aiogram.dispatcher import FSMContext
from loader import dp
from aiogram.types import CallbackQuery
from handlers.quran_api import Audio, Arab, Lotin, Tarjima
from keyboards.inline.suralar_oraligi_keyboard import sura_va_raqam
from states.oyat_state import State_oyat
from keyboards.inline.oyat_keyboard import Oyat_oraliq, Oyat_boshi, Oyat_oxiri



########################################################################################################################
##################  bu yerda suraning raqamini handler ushlab oladi va javob beradi  ###################################
########################################################################################################################
@dp.callback_query_handler(sura_va_raqam.filter())
async def Suralar(call: CallbackQuery, callback_data: dict, state: FSMContext):
    sura_raqami = callback_data.get('raqam')
    sura_nomi = callback_data.get('sura_nomi')
    msg = f"{sura_nomi} Surasi."
    await call.message.answer(msg)
    emoj = await call.message.answer("⏳")

    ######## audio ni faqat 1-oyatini, qolganlarini umumiy surani chaqirib olayapmiz ###################################
    audio = await Audio(sura_raqami)
    arab, oyatlar_soni = await Arab(sura_raqami)
    lotin = await Lotin(sura_raqami)
    tarjima = await Tarjima(sura_raqami)
    #######  Text tuzib olayapmiz ######################################################################################
    text = f"<b>{sura_nomi}. {oyatlar_soni} oyatdan iborat</b>\n"
    text += f"<b>{sura_raqami}-Sura 1-Oyat</b>\n"
    text += f"<b>{arab[0]}</b>\n{lotin[0]}\n\n{tarjima[0]}"
    ###### state data ga joylayapmiz pastdagi holatda ishlatamiz #######################################################
    await state.update_data(sura_raqami=sura_raqami)
    await state.update_data(sura_nomi=sura_nomi)
    await state.update_data(oyat_raqami=0)
    await state.update_data(oyatlar_soni=oyatlar_soni)
    await state.update_data(audio=audio)
    await state.update_data(arab=arab)
    await state.update_data(lotin=lotin)
    await state.update_data(tarjima=tarjima)
    ###### Foydalanuvchiga xabarlarni yuborayapmiz #####################################################################

    await emoj.delete()
    await call.message.answer_audio(audio[0])
    await call.message.answer(text, reply_markup=Oyat_boshi)
    await State_oyat.oyat.set()
########################################################################################################################
#############################    Handler tugashi    ####################################################################
########################################################################################################################





########################################################################################################################
##################  bu yerda oyatning raqamini handler ushlab oladi va javob beradi  ###################################
########################################################################################################################
@dp.callback_query_handler(state=State_oyat.oyat)
async def Oyatlar(call: CallbackQuery, state: FSMContext):
    text = call.data
    ##### state data ni ochayapti  #####################################################################################
    data = await state.get_data()
    #### malumotlarni olayapmiz    #####################################################################################
    sura_raqami = int(data.get("sura_raqami"))
    sura_nomi = data.get("sura_nomi")
    oyat_raqami = int(data.get("oyat_raqami"))
    oyatlar_soni = int(data.get("oyatlar_soni"))
    audio = data.get("audio")
    arab = data.get("arab")
    lotin = data.get("lotin")
    tarjima = data.get("tarjima")
    #####  if yani shu belgi kelsa keyingi oyatni yubor deyapman shunaqa  ##############################################
    if text == "➡️":
        ##### bu usha oxirgi oyat kelsa reply markup ni uzgartir yani yana keyingi oyatmas orqaga qaytish bitta markup##
        if oyat_raqami == oyatlar_soni-2:
            oyat_raqami +=1
            #### text tuzib olayapmiz  #################################################################################
            text = f"<b>{sura_nomi}. {oyatlar_soni} oyatdan iborat</b>\n"
            text += f"<b>{sura_raqami}-Sura {oyat_raqami+1}-Oyat</b>\n"
            text += f"<b>{arab[oyat_raqami]}</b>\n{lotin[oyat_raqami]}\n\n{tarjima[oyat_raqami]}"
            #### oyat raqami uzgargani uchun state qilib keyingi xolatga utkazib quyamiz ###############################
            await state.update_data(oyat_raqami=oyat_raqami)
            ###### Foydalanuvchiga xabarlarni yuborayapmiz #############################################################
            await call.message.answer_audio(audio[oyat_raqami])
            await call.message.answer(text, reply_markup=Oyat_oxiri)
            await State_oyat.oyat.set()
            time.sleep(0.001)


        else:   #####  else  keyingi oyatni yubor deyapman shunaqa  ####################################################
            oyat_raqami += 1
            #### text tuzib olayapmiz
            text = f"<b>{sura_nomi}. {oyatlar_soni} oyatdan iborat</b>\n"
            text += f"<b>{sura_raqami}-Sura {oyat_raqami+1}-Oyat</b>\n"
            text += f"<b>{arab[oyat_raqami]}</b>\n{lotin[oyat_raqami]}\n\n{tarjima[oyat_raqami]}"
            #### oyat raqami uzgargani uchun state qilib keyingi xolatga utkazib quyamiz ###############################
            await state.update_data(oyat_raqami=oyat_raqami)
            ###### Foydalanuvchiga xabarlarni yuborayapmiz #############################################################
            await call.message.answer_audio(audio[oyat_raqami])
            await call.message.answer(text, reply_markup=Oyat_oraliq)
            await State_oyat.oyat.set()
            time.sleep(0.001)

    #####  elif yani shu belgi kelsa bitta orqadagi oyatni qaytar deyapman #############################################
    elif text == "⬅️":
        ##### bu if yani boshidagi oyat yani birinchi oyat bolsa reply markup bitta boladi faqat oldiga ################
        if oyat_raqami == 1:
            oyat_raqami -= 1
            #### text tuzib olayapmiz
            text = f"<b>{sura_nomi}. {oyatlar_soni} oyatdan iborat</b>\n"
            text += f"<b>{sura_raqami}-Sura {oyat_raqami+1}-Oyat</b>\n"
            text += f"<b>{arab[oyat_raqami]}</b>\n{lotin[oyat_raqami]}\n\n{tarjima[oyat_raqami]}"
            #### oyat raqami uzgargani uchun state qilib keyingi xolatga utkazib quyamiz ###############################
            await state.update_data(oyat_raqami=oyat_raqami)
            ###### Foydalanuvchiga xabarlarni yuborayapmiz #############################################################
            await call.message.answer_audio(audio[oyat_raqami])
            await call.message.answer(text, reply_markup=Oyat_boshi)
            await State_oyat.oyat.set()
            time.sleep(0.001)

        else:   #####  else 1 ta orqadagi oyatni yubor deyapman shunaqa  ###############################################
            oyat_raqami -= 1
            #### text tuzib olayapmiz
            text = f"<b>{sura_nomi}. {oyatlar_soni} oyatdan iborat</b>\n"
            text += f"<b>{sura_raqami}-Sura {oyat_raqami+1}-Oyat</b>\n"
            text += f"<b>{arab[oyat_raqami]}</b>\n{lotin[oyat_raqami]}\n\n{tarjima[oyat_raqami]}"
            #### oyat raqami uzgargani uchun state qilib keyingi xolatga utkazib quyamiz ###############################
            await state.update_data(oyat_raqami=oyat_raqami)
            ###### Foydalanuvchiga xabarlarni yuborayapmiz #############################################################
            await call.message.answer_audio(audio[oyat_raqami])
            await call.message.answer(text, reply_markup=Oyat_oraliq)
            await State_oyat.oyat.set()
            time.sleep(0.001)

########################################################################################################################
#############################    Handler tugashi    ####################################################################
########################################################################################################################
