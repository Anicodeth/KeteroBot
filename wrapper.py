
from telegram import  KeyboardButton, ReplyKeyboardMarkup, Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_markup = ReplyKeyboardMarkup([

        [KeyboardButton("Sign Up", web_app=WebAppInfo(url="https://ketero-web.vercel.app/signup/client")), 
         KeyboardButton("Sign In", web_app=WebAppInfo(url="https://ketero-web.vercel.app/signin"))],
         
    ])
    await update.message.reply_text(
        "Welcome, Start Using Ketero In Seconds",
        reply_markup=reply_markup,
    )


def main() -> None:
    application = Application.builder().token("6672011144:AAHCySVm-SsHYbQ4mpHC54p1hXIwtBmYw1Y").build()

    application.add_handler(CommandHandler("start", start))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()