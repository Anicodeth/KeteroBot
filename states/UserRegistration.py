from aiogram.fsm.state import State, StatesGroup


class UserRegistration(StatesGroup):
    user_id = State()
    full_name = State()
    phone_number = State()
    email = State()

