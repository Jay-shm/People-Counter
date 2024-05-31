from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext, CallbackQueryHandler

TOKEN = "7300265655:AAG_PM3ws9pfRB0shTznCAMogNJbC-77ikk"
MINIAPP = "t.me/RoomPeopleCounter_Bot/ThePeopleCounter"
BOT_USERNAME = "@RoomPeopleCounter_Bot"

async def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Start", url=MINIAPP)],
        [InlineKeyboardButton("Follow On Instagram", url="https://www.instagram.com/jay_.rane/")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        f"""Hi! {update.message.chat.first_name}, 
            Let's get counting!
            Use /start to start.
            Use /count to try the app.
            Use /help to see all the commands.
            """, reply_markup=reply_markup)

async def count(update: Update, context: CallbackContext):
    await update.message.reply_text("t.me/RoomPeopleCounter_Bot/ThePeopleCounter")

async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text(
        """Available commands:
            /start - Start the bot.
            /count - Try the app.
            /help - See all the commands.
            """)

def main():
    builder = ApplicationBuilder().token(TOKEN).build()
    builder.add_handler(CommandHandler("start", start))
    builder.add_handler(CommandHandler("count", count))
    builder.add_handler(CommandHandler("help", help_command))
    builder.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, start))
    builder.add_handler(MessageHandler(filters.COMMAND, start))
    app = builder
    app.run_polling()

if __name__ == '__main__':
    main()
