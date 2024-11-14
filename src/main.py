from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from commands import start
from handler import button_handler
from config.config import BOT_TOKEN


app = ApplicationBuilder().token(BOT_TOKEN).build()

# Добавляем обработчики команд
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

# Запуск бота
app.run_polling()
