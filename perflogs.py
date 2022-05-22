from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import token #импортируем библиотеки и токен

bot = Bot(token=token) #токен сам
dp = Dispatcher(bot) #диспетчер сообщений

@dp.message_handler(commands=['start'])  #комманда /start

async def start_commands(message: types.Message): #функция сообщение, которое отвечает на комманду /start
	await message.reply("Hello bro") 
@dp.message_handler(commands=['help']) #комманда /help
async def help_commands(message: types.Message): #функция сообщение, которое отвечает на комманду /help
	await message.reply("I'm echo bot")

@dp.message_handler() #и сам эхо бот

async def echo_bot(msg: types.Message):
	await bot.send_message(msg.from_user.id, msg.text)

if __name__ == '__main__':
    executor.start_polling(dp) #бесконечный пуллинг диспетчера