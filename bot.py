import asyncio
from asyncio import get_event_loop

from steam_parser import pars
from aiogram import Bot, Dispatcher, executor, types
import logging

# ------------------------------------------------------------------------------- #
API_TOKEN = 'token from @BotFather'

bot = Bot(token=API_TOKEN, parse_mode="html")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

user_data = []
# ------------------------------------------------------------------------------- #


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    id = message.from_user.id
    if id not in user_data:
        user_data.append(id)
    games = pars()
    if games:
        for game, url in games.items():
            await message.answer(f"<b>Сегодня раздаётся <a href='{url}'>{game}</a></b>")
    else:
        await message.answer('<i>Сегодня раздачи нет</i>, но если она будет, бот вас оповестит! ')


async def bot_echo():
    while True:
        for id in user_data:
            games = pars()
            if games:
                for game, url in games.items():
                    await bot.send_message(chat_id=id, text=f"<b>Сегодня раздаётся <a href='{url}'>{game}</a></b>")
        await asyncio.sleep(3600 * 12)

# ------------------------------------------------------------------------------- #

if __name__ == '__main__':
    get_event_loop().create_task(bot_echo())
    executor.start_polling(dp, skip_updates=True)
