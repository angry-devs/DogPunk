from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from pydantic import BaseModel
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
db = SessionLocal()
class UserBase(BaseModel):
    name: str
class UserCreate(UserBase):
    name: str
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    # items = relationship("Item", back_populates="owner")
    
# Define the bot token
TOKEN = "8034896068:AAEqw3uC1DT9uTd2KJiV-3dU8bzYLtKGeeY"

def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()
async def send_message_with_link(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("crear", url="http://localhost:5173")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("crear un anucio:", reply_markup=reply_markup)

def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()
    start_handler = CommandHandler("crear_anuncio", send_message_with_link)
    application.add_handler(start_handler)
    application.run_polling()



if __name__ == "__main__":
    main()


# import logging
# from telegram import ForceReply, Update
# from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
# )
# logging.getLogger("httpx").setLevel(logging.WARNING)
# logger = logging.getLogger(__name__)
# async def crea_anuncio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

#     """Send a message when the command /start is issued."""

#     user = update.effective_user

#     await update.message.reply_html(

#         rf"Hi {user.mention_html()}!. Use the this link to create an ad: http://localhost:5173",

#         reply_markup=ForceReply(selective=True),

#     )



# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

#     """Send a message when the command /help is issued."""

#     await update.message.reply_text("Help!")



# async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Echo the user message."""
#     await update.message.reply_text(update.message.text)



# def main() -> None:

#     """Start the bot."""

#     # Create the Application and pass it your bot's token.

#     application = Application.builder().token("8034896068:AAEqw3uC1DT9uTd2KJiV-3dU8bzYLtKGeeY").build()


#     # on different commands - answer in Telegram

#     application.add_handler(CommandHandler("crea_anuncio", crea_anuncio))

#     application.add_handler(CommandHandler("help", help_command))


#     # on non command i.e message - echo the message on Telegram

#     application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))


#     # Run the bot until the user presses Ctrl-C

#     application.run_polling(allowed_updates=Update.ALL_TYPES)



# if __name__ == "__main__":
#     main()

