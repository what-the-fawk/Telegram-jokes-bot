import logging
import pyjokes
import time
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5882713162:AAFuJyyVERy_fIeJjyOaCwVFKOK6LyuY5Nk'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

history = set()
category = 'neutral'


@dp.message_handler(commands=['start'])
async def msg_start(message: types.Message):
    await message.answer("Welcome! Type /info for more information")


@dp.message_handler(commands=['info'])
async def msg_start(message: types.Message):
    await message.answer(
        "Hi! This bot is designed for giving unique(up to dictionary size ofc)"
        " jokes for programmers and everyone related.\n"
        "Jokes are also categorised, by default they are neutral"
        "Type /help to see list of commands available")


@dp.message_handler(commands=['help'])
async def msg_help(message: types.Message):
    await message.answer("List of commands:\n"
                         "/info - short info about bot"
                         "/start - basic start command\n"
                         "/help - shows list of commands\n"
                         "/joke - get free joke\n"
                         "/history - history of jokes (yes)\n"
                         "/reset - deletes history(auto-resets when necessary\n)"
                         "/category <NAME> - set category of jokes\n"
                         "/category_list - list of categories")


@dp.message_handler(commands=['category_list'])
async def msg_start(message: types.Message):
    await message.answer("List of categories: chuck, neutral, all")


@dp.message_handler(commands=['reset'])
async def msg_start(message: types.Message):
    history.clear()
    await message.answer("Reset done")


@dp.message_handler(commands='category', regexp='chuck')
async def msg_start(message: types.Message):
    global category
    category = 'chuck'
    # category.join('chuck')
    await message.answer(f"Category set to {category}")


@dp.message_handler(commands='category', regexp='neutral')
async def msg_start(message: types.Message):
    global category
    category = 'neutral'
    # category.join('chuck')
    await message.answer(f"Category set to {category}")


@dp.message_handler(commands='category', regexp='all')
async def msg_start(message: types.Message):
    global category
    category = 'all'
    # category.join('chuck')
    await message.answer(f"Category set to {category}")


@dp.message_handler(commands='category')
async def msg_start(message: types.Message):
    await message.answer("Wrong category name")


@dp.message_handler(commands=['joke'])
async def send_welcome(message: types.Message):
    joke = pyjokes.get_joke('en', category)
    reset = False
    start_time = time.time()
    while joke in history:
        joke = pyjokes.get_joke('en', category)

        if time.time() - start_time > 3:
            reset = True
            break

    if reset:
        await message.answer("Reset done, get your jokes again!")
        history.clear()

    history.add(joke)
    await message.answer(joke)


@dp.message_handler(commands=None)
async def command_unknown(message: types.Message):
    if message.text == "Why so serious":
        await message.answer("Seems ur Joker fan, appreciate it")
    else:
        await message.answer("Unknown command, Type /help for list of commands")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
