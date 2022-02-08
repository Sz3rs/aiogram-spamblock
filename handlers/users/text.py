from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from models.user import User
from loader import dp
from os import getenv


@dp.message_handler()
async def bot_text(msg: types.Message) -> None:
    User.get_or_create(id=msg.from_user.id)
    try:
        f_message = await msg.forward(getenv('adminId'))
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Ответить', callback_data=f'answer|{msg.from_user.id}'))

        if msg.from_user.username:
            answer_text = '@' + msg.from_user.username
        else:
            answer_text = f"<a href='tg://user?id={msg.from_user.id}'>{msg.from_user.id}</a>"

        await f_message.reply(answer_text, reply_markup=keyboard, parse_mode='HTML')
    except Exception as e:
        print(e)
    await msg.answer(f"Спасибо! Я обязательно отвечу тебе с основного аккаунта.")
