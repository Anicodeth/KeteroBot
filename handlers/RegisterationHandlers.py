
from aiogram.filters import  CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    Contact
)
from aiogram.types.web_app_info import WebAppInfo
from states.ServiceBooking import ServiceBooking
from states.UserRegistration import UserRegistration
from configs.botConfig import form_router
    
@form_router.message(CommandStart())
async def command_start( message: Message, state: FSMContext) -> None:

    # await message.answer(f"Thanks, please share your phone number (use the 'Share my phone number' feature).",
    # reply_markup=ReplyKeyboardMarkup(
    #                         keyboard=[
    #                             [KeyboardButton(text="Google", web_app=WebAppInfo(url="http://www.google.com"))],
    #                         ],
    #                         resize_keyboard=True
    #                     )
    #                   )
    await message.answer("Welcome to the KeteroBot! I will guide you through the registration process. Please provide your full name.")
    
    await state.set_state(UserRegistration.full_name)

# @form_router.message(CommandStart())
# async def command_start( message: Message, state: FSMContext) -> None:
#     await message.answer("Welcome Back, Here are our services")
#     await state.set_state(ServiceBooking.get_businesses)


@form_router.message(UserRegistration.full_name)
async def process_full_name(message: Message, state: FSMContext):
    if not message.text:
        await message.answer("Please provide a valid full name.")
        return
    await state.update_data(full_name=message.text)
    data = await state.get_data()

    await message.answer(f"Thanks, {data['full_name']}! Now, please share your phone number (use the 'Share my phone number' feature).",
    reply_markup=ReplyKeyboardMarkup(
                            keyboard=[
                                [KeyboardButton(text="Share my phone number", request_contact=True)],
                            ],
                            resize_keyboard=True
                        )
                        )

    await state.set_state(UserRegistration.phone_number)

@form_router.message(UserRegistration.phone_number)
async def process_phone_number(message: Contact, state: FSMContext):
    print(message.contact)
    user_id = message.contact.user_id  # Use Telegram user ID as primary key
    await state.update_data(user_id=user_id)
    phone_number = message.contact.phone_number
    await state.update_data(phone_number=phone_number)
    await message.answer("Great! Now provide your email")


    await state.set_state(UserRegistration.email)

@form_router.message(UserRegistration.email)
async def process_role(message: Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    
    # Retrieve user data from state
    data = await state.get_data()

    await message.answer(f"Registration complete!\n\n"
                        f"Full Name: {data['full_name']}\n"
                        f"Phone Number: {data['phone_number']}\n"
                        f"Email: {data['email']}\n\n"
                        "You are now signed up!")

    # Finish the registration process and reset the state
    await state.clear()