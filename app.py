import sys
import asyncio
import logging

from aiogram import F
from aiogram import Bot
from aiogram import types
from aiogram import Dispatcher

from aiogram.filters import CommandStart

from aiogram.types import Message
from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup


TOKEN = "6324232749:AAHQZE62IuPsV97ugB4lXitRoaXbyLxBw_A"


# Initialize Dispatcher
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        "Demo started",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Go to form", callback_data="start")] # noqa
            ]
        ),
    )


@dp.callback_query(F.data.startswith('start'))
async def first(callback_query: types.CallbackQuery):
    await callback_query.message.answer('Хорошо, приступим ко второму вопросу.') # noqa


@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
