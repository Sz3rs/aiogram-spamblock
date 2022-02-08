from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from models.user import User
from loader import dp, bot
from os import getenv
from aiogram.dispatcher import FSMContext
from states.answer import AdminAnswer


@dp.callback_query_handler(text_startswith="answer|")
async def admin_answer_request(call: types.CallbackQuery, state: FSMContext) -> None:
    if str(call.from_user.id) == str(getenv('adminId')):
        await state.finish()
        await AdminAnswer.waiting_text.set()
        await state.update_data(chat_id=call.data.split('answer|')[1])

        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Отмена', callback_data='cancel'))

        await call.message.reply('Введите ответ: ', reply_markup=keyboard)


@dp.message_handler(state=AdminAnswer.waiting_text)
async def admin_answer(msg: types.Message, state: FSMContext) -> None:
    user_data = await state.get_data()
    try:
        await bot.send_message(user_data.get('chat_id'), msg.text, entities=msg.entities)
        await msg.reply('Отправлено!')
    except Exception as e:
        await msg.reply('Ошибка отправки: ' + str(e))

    await state.finish()


@dp.callback_query_handler(text_contains='cancel', state=AdminAnswer.waiting_text)
async def admin_cancel_answer(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('Отменено!')