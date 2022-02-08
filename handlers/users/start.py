from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from models.user import User
from loader import dp


@dp.message_handler(CommandStart(), state='*')
async def bot_start(msg: types.Message) -> None:
    User.get_or_create(id=msg.from_user.id)
    await msg.answer(f"👋 Привет, {msg.from_user.first_name}\n"
                     f"Напиши мне сообщение, и я отвечу тебе с основного аккаунта!")
