from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnGenerateGachi = KeyboardButton('Generate Gachi')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnGenerateGachi)
