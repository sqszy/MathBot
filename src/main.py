import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from config.config import BOT_TOKEN
from commands import start
from handlers.teorems import button_handler
from handlers.ocr import ai_handler

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s "
        "[%(asctime)s] - %(name)s - %(message)s",
    )

    logger.info("Starting bot")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Добавляем обработчики команд
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.PHOTO | filters.TEXT & ~filters.COMMAND, ai_handler))

    logger.info("Bot started. Press Ctrl+C to stop.")
    # Запуск бота
    app.run_polling(allowed_updates=Update.ALL_TYPES)
    logger.info("Bot stoped")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")
