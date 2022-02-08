from aiogram.dispatcher.filters.state import State, StatesGroup


class AdminAnswer(StatesGroup):
    waiting_text = State()
