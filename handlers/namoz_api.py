import requests
from bs4 import BeautifulSoup
from PIL import Image,  ImageDraw, ImageFont
import datetime as dt


def namoz(id):
    url = "https://namozvaqtlari.com/"
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "referer": "https://www.google.com/"
    }
    site = requests.get(url=url, headers=headers)
    htmldom = BeautifulSoup(site.text, "lxml")
    resp = htmldom.findAll("div", class_ = "info")
    namoz_lst = []
    for n in resp:
        n = n.find("p")
        namoz_lst.append(n.text.strip())
    #  image chaqirib olayapmiz
    image = Image.open('rasmlar/namoz.png')
    draw = ImageDraw.Draw(image)
    # data time di chaqirish
    hozir=dt.datetime.now()
    sana=hozir.date()
    # bu data time yani sana yozilayapti
    sana_font = ImageFont.truetype("rasmlar/arial2.TTF", 50)
    draw.text((570, 410), f'{sana}', font=sana_font, fill=(0, 0, 0))
    # bu namoz vaqtlari
    vaqt_font = ImageFont.truetype("rasmlar/arial2.TTF", 60)
    draw.text((110, 610), f"{namoz_lst[0]}", font=vaqt_font, fill=(0, 0, 0)) # bomdod
    draw.text((445, 610), f"{namoz_lst[1]}", font=vaqt_font, fill=(0, 0, 0))  # quyosh
    draw.text((775, 610), f"{namoz_lst[2]}", font=vaqt_font, fill=(0, 0, 0))  # peshin
    draw.text((110, 795), f"{namoz_lst[3]}", font=vaqt_font, fill=(0, 0, 0))  # asr
    draw.text((440, 795), f"{namoz_lst[4]}", font=vaqt_font, fill=(0, 0, 0)) # shom
    draw.text((775, 795), f"{namoz_lst[5]}", font=vaqt_font, fill=(0, 0, 0))   # xufton
    # rasmga namoz vaqtlarini yozib uni saqlayapmiz yani shu id raqam nomi bilan
    image.save(f'rasmlar/{id}.png')



