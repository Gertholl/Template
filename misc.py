import config
from aiogram import Bot, Dispatcher
import logging
logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)