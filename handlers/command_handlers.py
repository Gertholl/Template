from misc import bot, dp
from aiogram.types import  Message, CallbackQuery
from keyboards import defult as keyboard



@dp.message_handler(commands=['start'])
async def start(message: Message):
   await bot.send_message(message.from_user.id, text='Бот для размещения точек бурения скважин', reply_markup=keyboard.start_menu())

