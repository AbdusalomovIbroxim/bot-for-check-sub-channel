from aiogram import types, Bot, Dispatcher, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import logging

logging.basicConfig(level=logging.INFO)
bot = Bot(token='5481867724:AAE_mHwPMBp9z6cneAqopmXc5w3mEAQOdTo')
dp = Dispatcher(bot)


async def on_startup(_):
    print('Bot online')


channel_url = 'https://t.me/Test_2a'
channel_id = '@Test_2a'
chat_id = '@Test_2a_a'

btn = InlineKeyboardMarkup(row_width=1)
kanal = InlineKeyboardButton(text='Kanal', url=channel_url)
btn.insert(kanal)


def check_sub_channel(chat_member):
    return chat_member['status'] != 'left'


@dp.message_handler()
async def mess_handler(message: types.Message):
    # msg = await message.answer('+')
    m_id = message.message_id
    if not check_sub_channel(await bot.get_chat_member(chat_id=channel_id, user_id=message.from_user.id)):
        await bot.delete_message(message.chat.id, m_id)
        await message.answer("SMS yozish uchun kanalga azo bo'ling!", reply_markup=btn)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
