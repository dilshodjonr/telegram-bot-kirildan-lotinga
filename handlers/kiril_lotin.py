# from aiogram import Router, F
# from aiogram.types import Message, chat_member_updated
# from aiogram.types.chat_member import ChatMember

# translite_router: Router = Router()

# from handlers.transliterate import to_cyrillic, to_latin, transliterate

# import regex

# def latinOrCyrillic(text):
#     check = bool(regex.search(r'\p{IsCyrillic}', text))
#     if check == True:
#         result = to_latin(text)
#     else :
#         result = to_cyrillic(text)
#     return result

# @translite_router.message()
# async def latin(msg: Message):
#     await msg.answer(latinOrCyrillic(msg.text))

import regex  # Regex kutubxonasi kerak

from aiogram import Router
from aiogram.types import Message

from handlers.transliterate import to_cyrillic, to_latin  # Eski kodimizdan funksiyalarni chaqiramiz

translite_router: Router = Router()

def latinOrCyrillic(text):
    # Tekshirish
    check = regex.search(r'\p{IsCyrillic}', text)
    if check:  # Agar kirilcha bo'lsa
        result = to_latin(text)  # Kirilchani lotinchaga aylantiramiz
    else:
        result = to_cyrillic(text)  # Aks holda lotincha kirilgacha aylantiramiz
    return result

@translite_router.message()
async def latin(msg: Message):
    try:
        await msg.answer(latinOrCyrillic(msg.text))  # Xabarni o'zgartirish
    except Exception as e:
        await msg.answer(f"Hatolik: {e}")  # Xatolikni qaytarish