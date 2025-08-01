from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Replace with your bot token
BOT_TOKEN = "8108498513:AAGfpszLJ1WrzFYi6LHcKwbR12BAvoD_9uM"
ADMIN_ID = 6588434606

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 আমি অনলাইনে আছি! কিভাবে সাহায্য করতে পারি?")

async def reply_all_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text
    user = update.effective_user.first_name
    print(f"Message from {user}: {message}")

    # Forward message to Admin (optional)
    await context.bot.send_message(chat_id=ADMIN_ID, text=f"📩 {user}: {message}")

    # Auto reply to user
    await update.message.reply_text("✅ আপনার মেসেজ পেয়েছি। শিগগিরই উত্তর দেওয়া হবে।")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_all_messages))

    print("Bot is running...")
    app.run_polling()
