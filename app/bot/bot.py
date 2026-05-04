from telegram.ext import Application
from core.config import settings
from bot.handlers import handle_info_to_send
telegram_app = None

async def init_telegram_bot():
    global telegram_app
    print("bot initialization")
    
    # Initialize the application
    telegram_app = Application.builder().token(settings.BOT_TOKEN).build()
    # Start the bot in the existing event loop
    await telegram_app.initialize()
    await telegram_app.updater.start_polling()
    await telegram_app.start()
    print("Bot started successfully")

async def send_info_to_manager(ai_result: dict):
    manager_telegram_id,message = handle_info_to_send(ai_result)
    await telegram_app.bot.send_message(
        chat_id=manager_telegram_id,
        text=message,
        parse_mode="HTML"
    )

async def stop_telegram_bot():
    global telegram_app
    if telegram_app:
        print("Stopping bot...")
        await telegram_app.updater.stop()
        await telegram_app.stop()
        await telegram_app.shutdown()