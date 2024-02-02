
from aiogram.filters import  CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    Contact
)
from states.ServiceBooking import ServiceBooking
from configs.botConfig import form_router

@form_router.message(ServiceBooking.get_businesses)
async def get_businesses(message: Message, state: FSMContext):
    # Implement logic to fetch and display available businesses
    # For example, you can use InlineKeyboardMarkup to create a list of businesses
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("Business A"))
    keyboard.add(KeyboardButton("Business B"))

    await message.answer("Choose a business to book services:", reply_markup=keyboard)
    await ServiceBooking.select_services.set()

selected_services_dict = {}
@form_router.message(ServiceBooking.select_services)
async def select_services(message: Message, state: FSMContext):
    # Retrieve available services (you might fetch this from a database)
    available_services = ["Service 1", "Service 2", "Service 3"]

    # Get the user's ID
    user_id = message.from_user.id

    # Check if the user already has selected services stored in the dictionary
    if user_id not in selected_services_dict:
        selected_services_dict[user_id] = set()

    # Create a custom keyboard with services as buttons
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for service in available_services:
        # Check if the service is already selected for this user
        if service in selected_services_dict[user_id]:
            button_text = f"✅ {service}"
        else:
            button_text = f"❌ {service}"

        keyboard.add(KeyboardButton(button_text))

    # Add a button to confirm the selection
    keyboard.add(KeyboardButton("Confirm Selection"))

    await message.answer("Choose services to book:", reply_markup=keyboard)

@form_router.message(ServiceBooking.select_services)
async def handle_service_selection(message: Message, state: FSMContext):
    # Retrieve user's ID and selected services
    user_id = message.from_user.id
    selected_service = message.text

    # Check if the user clicked on the "Confirm Selection" button
    if selected_service == "Confirm Selection":
        # Proceed to the next state or handle confirmation logic
        await message.answer("Please proceed to make a down payment.")
        await ServiceBooking.down_payment.set()
    else:
        # Toggle the selected state for the service
        if selected_service.startswith("✅"):
            selected_services_dict[user_id].remove(selected_service[2:])
        else:
            selected_services_dict[user_id].add(selected_service[2:])

        # Update the message with the updated keyboard
        await select_services(message, state)

@form_router.message(ServiceBooking.book_services)
async def book_services(message: Message, state: FSMContext):
    # Implement logic to handle the booking process
    # You can update the state or store the selected services in the database
    selected_services = message.text  # Replace this with your logic

    await message.answer(f"You have selected the following services: {selected_services}")
    await message.answer("Please proceed to make a down payment.")
    await ServiceBooking.down_payment.set()

@form_router.message(ServiceBooking.down_payment)
async def down_payment(message: Message, state: FSMContext):
    # Implement logic for down payment
    # You can finalize the booking process and reset the state
    await message.answer("Thank you for your payment! Your services are booked.")
    await state.finish()
