import logging
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)
async def crea_anuncio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    """Send a message when the command /start is issued."""

    user = update.effective_user

    await update.message.reply_html(

        rf"Hi {user.mention_html()}!. Use the this link to create an ad: http://localhost:5173",

        reply_markup=ForceReply(selective=True),

    )
async def send_periodic_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = "This is a periodic message sent every 30 minutes."
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)

async def post_anuncio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    """Send a message when the command /start is issued."""

    user = update.effective_user

    await update.message.reply_html(

        rf"Hi {user.mention_html()}!. Use the this link to create an ad: http://localhost:5173",

        reply_markup=ForceReply(selective=True),

    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    """Send a message when the command /help is issued."""

    await update.message.reply_text("Help!")



async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)



def main() -> None:

    """Start the bot."""

    # Create the Application and pass it your bot's token.

    application = Application.builder().token("8034896068:AAEqw3uC1DT9uTd2KJiV-3dU8bzYLtKGeeY").build()


    # on different commands - answer in Telegram

    application.add_handler(CommandHandler("crea_anuncio", crea_anuncio))

    application.add_handler(CommandHandler("help", help_command))


    # on non command i.e message - echo the message on Telegram

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    job_queue = application.job_queue
    job_queue.run_repeating(send_periodic_message, interval=1000, first=0)
job = context.job_queue.run_repeating(callback, interval=5)
    # Run the bot until the user presses Ctrl-C

    application.run_polling(allowed_updates=Update.ALL_TYPES)



if __name__ == "__main__":
    main()

