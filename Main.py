from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio
import random
import os
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TOKEN:
    raise SystemExit("Ошибка: Токен не найден! Добавь его в .env")

def main_kb():
    builder = InlineKeyboardBuilder()
    builder.button(text="Play", callback_data=kb_callback(action="play").pack())
    builder.button(text="Info", callback_data=kb_callback(action="info").pack())
    builder.button(text="Cat", callback_data=kb_callback(action="cat").pack())
    builder.button(text="Dog", callback_data=kb_callback(action="dog").pack())

    return builder.as_markup()

class kb_callback(CallbackData, prefix='name'):
    action: str

random_sticker_list = [
    'CAACAgIAAxkBAAIEWWj8yspFJ4bT7P_H_foSGE2-R70oAAKpZgACQwJxSov50HGT4hv_NgQ',
    'CAACAgIAAxkBAAIEX2j8y2GjlNCLSrTIGHnjxotWEpavAAJQagACFrZoSgrU4pSuPs8UNgQ',
    'CAACAgIAAxkBAAIEYWj8y2IS2EnWi5gtQNZAqSfifMtJAALqawACtPtxSryKg4VVIxc8NgQ',
    'CAACAgIAAxkBAAIEY2j8y2QK5q_r2Nr7MMsqUr9vQ0YAA5ZwAALPvHBKk42-bhqPfhg2BA',
    'CAACAgIAAxkBAAIEZWj8y2XvOb6AgCjH6Pu7E0kdK0D6AAIycgACZWtwSljDaUGRpk6uNgQ',
    'CAACAgIAAxkBAAIEZ2j8y2cG7-V4QDVsXyrnQp60LhGQAAIVbAACpWxpSly3peZJ7oZ5NgQ'
]

random_kurosaki_sticker_list = [
     {'text': 'くろさき😎', 'sticker': 'CAACAgIAAxkBAAIEoGj8zQwxXNaCsTCatbTiMYTVsehHAAKaZQACQBNwSh5XTcpNfZ9mNgQ'},
     {'text': 'くろさき😩', 'sticker': 'CAACAgUAAxkBAAIEomj8zS4OO7KcgN148VNo7-LfuQbuAAKwEQACDuzRVap0jqL_7v9jNgQ'},
     {'text': 'くろさき🥵', 'sticker': 'CAACAgUAAxkBAAIEpGj8zTCoMHJ40k5VujPCoO66Kzl_AAIlEwACevnRVVHj2p2eIDzfNgQ'},
     {'text': 'くろさき🤯', 'sticker': 'CAACAgUAAxkBAAIEpmj8zTmDe9w5pwTybWCleuSpTXIDAAJsDwAC2BXYVWiOHA2-8WHcNgQ'}
]

random_aizen_sticker_list = [
    {"text": "", 'sticker': ''}
]



bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)

@router.message(CommandStart())
async def start_cmd(msg: types.Message):
    await msg.answer('Yahoo、ナルトちゃんにようこそ', reply_markup=main_kb())

@router.callback_query(kb_callback.filter())
async def main_cb(cb: types.CallbackQuery, callback_data: kb_callback):
    actions = callback_data.action

    if actions == 'play':
        await cb.answer()
        await cb.message.answer_sticker('CAACAgIAAxkBAAIEGWj6GX6FYKxAtaMbDGCkHP5VHFP4AAJzVQACz2iRSTuQ39S7sotrNgQ')
    elif actions == 'info':
        await cb.answer()
        await cb.message.answer('ようこそ')
    elif actions == 'cat':
        await cb.answer()
        await cb.message.answer_sticker('CAACAgIAAxkBAAIEF2j6GXgWVR8Zy7QDwiewg2WA935NAALhYQACTokhSowvquJfLBxRNgQ')
    elif actions == 'dog':
        await cb.answer()
        await cb.message.answer_sticker('CAACAgIAAxkBAAIEFWj6GW2uchz8MxneRBfYIDWarl24AALRXAACsZs4SdwijVCWewsgNgQ')

@router.message()
async def answer_cmd(msg: types.Message):
    text = msg.text.lower()
    if 'порн' and 'не' in text:
            await msg.answer_sticker('CAACAgIAAxkBAAIEWWj8yspFJ4bT7P_H_foSGE2-R70oAAKpZgACQwJxSov50HGT4hv_NgQ')
    elif'порн' in text:
            await msg.answer('へんたい！')
            await msg.answer_sticker('CAACAgIAAxkBAAIEKWj6H4TbKhfSO8VGtp2GXBbBkFVaAAKEYAAChp7ZSmqdTRPVuLwSNgQ')
    elif 'aizen' == text:
        await msg.answer('ようこそ、私の世界へ')
        await msg.answer_sticker('CAACAgIAAxkBAAIET2j6IkT39QxU2vm9WjqtnPqOdGZUAAIqZgACLz9oShsTSP-HXj6aNgQ')
    elif 'kurosaki' == text:
        random_kurosaki = random.choice(random_kurosaki_sticker_list)
        await msg.answer(random_kurosaki['text'])
        await msg.answer_sticker(random_kurosaki['sticker'])
    else:
        await msg.answer_sticker(random.choice(random_sticker_list))



async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())