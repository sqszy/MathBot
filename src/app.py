from telegram.ext import ApplicationBuilder, CommandHandler
from telegram import CallbackQueryHandler
from config.config import BOT_TOKEN
from commands import (
    start,
    pi,
    trapezoid,
    derivative,
    tablsquare,
    tablstep,
    square,
    rectangle,
    triangle,
    trapezoid,
    trigonometry,
    rhomb,
    parallelepiped,
    parallelogram,
    sphere,
    circle,
    cone,
    cube,
    pyramid,
)
from handler import button_handler

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("pi", pi))
app.add_handler(CommandHandler("trigonometry", trigonometry))
app.add_handler(CommandHandler("derivative", derivative))
app.add_handler(CommandHandler("tablstep", tablstep))
app.add_handler(CommandHandler("tablsquare", tablsquare))
app.add_handler(CommandHandler("square", square))
app.add_handler(CommandHandler("rectangle", rectangle))
app.add_handler(CommandHandler("triangle", triangle))
app.add_handler(CommandHandler("trapezoid", trapezoid))
app.add_handler(CommandHandler("rhomb", rhomb))
app.add_handler(CommandHandler("parallelogram", parallelogram))
app.add_handler(CommandHandler("sphere", sphere))
app.add_handler(CommandHandler("parallelepiped", parallelepiped))
app.add_handler(CommandHandler("circle", circle))
app.add_handler(CommandHandler("cone", cone))
app.add_handler(CommandHandler("pyramid", pyramid))
app.add_handler(CommandHandler("cube", cube))
app.add_handler(CallbackQueryHandler(button_handler))

# Запуск бота
app.run_polling()
