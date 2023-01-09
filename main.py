from aiogram import types, Bot, Dispatcher, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import logging

logging.basicConfig(level=logging.INFO)
bot = Bot(token='TOKEN')
dp = Dispatcher(bot)

channel_url = 'channel url'
channel_id = 'channel id'
chat_id = 'Droup id'

btn = InlineKeyboardMarkup(row_width=2)
kanal = InlineKeyboardButton(text='Kanal', url=channel_url)
btn.add(kanal)


def check_sub_channel(chat_member):
    return chat_member['status'] != 'left'


@dp.message_handler()
async def mess_handler(message: types.Message):
    m_id = message.message_id
    if not check_sub_channel(await bot.get_chat_member(chat_id=channel_id, user_id=message.from_user.id)):
        await bot.delete_message(message.chat.id, m_id)
        await bot.send_message(message.chat.id, "SMS yozish uchun kanalga azo bo'ling!", reply_markup=btn)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
