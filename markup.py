from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Main menu
btnGenerateGachi = KeyboardButton('Generate Gachi')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnGenerateGachi)
