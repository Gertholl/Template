from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton


def start_menu():
    menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='⛳️Координаты'),
                KeyboardButton(text='🗻Состав грунта'),
                KeyboardButton(text='📉Глубина'),

            ],
            [
                KeyboardButton(text='📈Высота'),
                KeyboardButton(text='🎯Точность'),
                KeyboardButton(text='📦Сохранить точку')
            ],
        ],
        resize_keyboard=True
    )

    return menu