import sys
import os

# Добавляем путь к родительской директории для правильного импорта
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from src.commands import start
from src.handler import button_handler
from src.config.config import BOT_TOKEN



app = ApplicationBuilder().token(BOT_TOKEN).build()


# Добавляем обработчики команд
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

# Запуск бота
app.run_polling()
