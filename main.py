import asyncio
import logging
import sys
from aiogram.enums import ParseMode

from aiogram import Bot, Dispatcher
from configs.botConfig import TOKEN, form_router
# from handlers.RegisterationHandlers import *
# from handlers.ServiceBookingHandlers import *
from aiogram.filters import  CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    Contact
)
from aiogram.types.web_app_info import WebAppInfo

@form_router.message(CommandStart())
async def command_start( message: Message, state: FSMContext) -> None:

    await message.answer(f"Start Using Ketero In Seconds ",
    reply_markup=ReplyKeyboardMarkup(
                            keyboard=[
                                [KeyboardButton(text="Sign Up", web_app=WebAppInfo(url="https://ketero-web.vercel.app/signup/client")),
                                 KeyboardButton(text="Sign In", web_app=WebAppInfo(url="https://ketero-web.vercel.app/signin"))],
                            ],
                            resize_keyboard=True
                        )
                      )

async def main():
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(form_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())