from aiogram.fsm.state import State, StatesGroup

class ServiceBooking(StatesGroup):
    get_businesses = State()
    select_services = State()
    book_services = State()
    down_payment = State()