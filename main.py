import os
import random

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv

import links
import markup as nav

load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Welcome to the club, {0.first_name}'.format(message.from_user),
                           reply_markup=nav.mainMenu)


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == 'Generate Gachi':
        await message.reply_photo(links.gachi[random.randint(0, len(links.gachi)-1)])
    else:
        await message.reply('Dude only gachi')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
