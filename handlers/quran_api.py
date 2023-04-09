import aiohttp





############################# Bu suraning hamma oyati Audiosini qaytaradi    ########################################
########################################################################################################################
async def get_audio(session, url):
    async with session.get(url) as resp:
        respons = await resp.json()
        return respons['data']['verses']


async def Audio(sura_id):
    async with aiohttp.ClientSession() as session:
        url = f"https://api.quran.gading.dev/surah/{sura_id}"
        verses = await get_audio(session, url)
        ##### lstga suraning hamma oyatlari audio linkini qushamiz
        audio_lst = []
        for audio in verses:
            audio_lst.append(audio['audio']['primary'])

        return audio_lst
########################################################################################################################
########################################################################################################################






############################# Bu suraning Arab oyatlarini va oyatlar_sonini lstga yozib qaytaradi  #####################
########################################################################################################################
async def get_arab(session, url):
    async with session.get(url) as resp:
        respons = await resp.json()
        return respons['chapter']

async def Arab(sura_id):
    async with aiohttp.ClientSession() as session:
        quran_arab = 'ara-quranbazzi'
        url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{quran_arab}/{sura_id}.json'
        chapter = await get_arab(session, url)
        ##### lstga arab tilidagi oyatlarni qushamiz
        arab_lst = []
        for oyat in chapter:
            arab_lst.append(oyat['text'])
        ##### oyatlar sonini qaytarayapmiz
        oyatlar_soni = len(chapter)

        return arab_lst, oyatlar_soni
########################################################################################################################
########################################################################################################################






############################# Bu suraning Lotin oyatlarini lstga yozib qaytaradi  ######################################
########################################################################################################################
async def get_lotin(session, url):
    async with session.get(url) as resp:
        respons = await resp.json()
        return respons['chapter']

async def Lotin(sura_id):
    async with aiohttp.ClientSession() as session:
        quran_lotin = 'ara-quran-la1'
        url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{quran_lotin}/{sura_id}.json'
        chapter = await get_lotin(session, url)
        ##### lstga lotin tilidagi oyatlarni qushamiz
        lotin_lst = []
        for oyat in chapter:
            lotin_lst.append(oyat['text'])

        return lotin_lst
########################################################################################################################
########################################################################################################################






############################# Bu suraning  oyatlari tarjimasini lstga yozib qaytaradi  #################################
########################################################################################################################
async def get_tarjima(session, url):
    async with session.get(url) as resp:
        respons = await resp.json()
        return respons['chapter']

async def Tarjima(sura_id):
    async with aiohttp.ClientSession() as session:
        quran_tarjima = 'uzb-muhammadsodikmu'
        url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{quran_tarjima}/{sura_id}.json'
        chapter = await get_tarjima(session, url)
        ##### lstga tarjima  oyatlarni qushamiz
        tarjima_lst = []
        for oyat in chapter:
            tarjima_lst.append(oyat['text'])

        return tarjima_lst
########################################################################################################################
########################################################################################################################