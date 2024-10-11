from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler,
)
from config import BOT_NAME, BOT_TOKEN

app = ApplicationBuilder().token(BOT_TOKEN).build()


# Объявляем команды
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Информация", callback_data="info")],
        [InlineKeyboardButton("Теоремы", callback_data="theorems")],
        [InlineKeyboardButton("Шпаргалки", callback_data="cheatsheets")],
        [InlineKeyboardButton("Решить задачу", callback_data="solve")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"Привет, {update.effective_user.first_name}! Я бот калькулятор, созданный на языке Python. Это курсовая работа по предмету - Технология программирования.",
        reply_markup=reply_markup,
    )


async def pi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="[Число Пи - 3,141592...]"
    )


async def trigonometry(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="[Основные тригонометрические тождества](https://telegra.ph/Osnovnye-trigonometricheskie-tozhdestva-10-11)",
        parse_mode="Markdown",
    )


async def derivative(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="[Производные](https://telegra.ph/Proizvodnye-10-11)",
        parse_mode="Markdown",
    )


async def tablstep(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="[Таблица степеней](https://telegra.ph/Tablica-stepenej-10-11)",
        parse_mode="Markdown",
    )


async def tablsquare(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="[Таблица квадратов](https://telegra.ph/Tablica-kvadratov-10-11)",
        parse_mode="Markdown",
    )


async def square(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="[\nКвадрат](https://telegra.ph/Kvadrat-10-11-3)",
        parse_mode="Markdown",
    )


async def rectangle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="[\nПрямоугольник](https://telegra.ph/Pryamougolnik-10-11)",
        parse_mode="Markdown",
    )


async def triangle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="[\nТреугольник](https://telegra.ph/Treugolnik-10-11)",
        parse_mode="Markdown",
    )


async def rhomb(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="[\nРомб](https://telegra.ph/Romb-10-11)",
        parse_mode="Markdown",
    )


async def trapezoid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="[\nТрапеция](https://telegra.ph/Trapeciya-10-11)",
        parse_mode="Markdown",
    )


async def parallelepiped(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="[\nПараллелепипед](https://telegra.ph/Parallelepiped-10-11)",
        parse_mode="Markdown",
    )


async def sphere(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="[\nСфера](https://telegra.ph/Sfera-10-11)",
        parse_mode="Markdown",
    )


async def parallelogram(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="[\nПараллелограмм](https://telegra.ph/Parallelogramm-10-11)",
        parse_mode="Markdown",
    )


async def circle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="[\nОкружность](https://telegra.ph/Okruzhnost-10-11)",
        parse_mode="Markdown",
    )


async def cone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="[\nCone](https://telegra.ph/Konus-10-11)",
        parse_mode="Markdown",
    )


async def pyramid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="[\npyramid](https://telegra.ph/Piramida-10-11-17)",
        parse_mode="Markdown",
    )


async def cube(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="[\nCube](https://telegra.ph/Kub-10-11)",
        parse_mode="Markdown",
    )


async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Привет, я студент 3 курса\nЕсли хочешь узнать как я это сделал и как устроен проект, напиши мне и я расскажу обо всём\nСсылка на мой аккаунт - "
        + "[@jjkxxd](https://t.me/jjkxxd)",
        parse_mode="Markdown",
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == "info":
        keyboard = [[InlineKeyboardButton("Назад", callback_data="back")]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(
            text="Привет, я студент 3 курса\nЕсли хочешь узнать как я это сделал и как устроен проект, напиши мне и я расскажу обо всём\nСсылка на мой аккаунт - [@jjkxxd](https://t.me/jjkxxd)",
            parse_mode="Markdown",
            reply_markup=reply_markup,
        )

    elif query.data == "theorems":
        keyboard = [[InlineKeyboardButton("Назад", callback_data="back")]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(
            text="Здесь будут теоремы...", reply_markup=reply_markup
        )

    elif query.data == "cheatsheets":
        keyboard = [[InlineKeyboardButton("Назад", callback_data="back")]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(
            text="Здесь будут шпаргалки...", reply_markup=reply_markup
        )

    elif query.data == "solve":
        keyboard = [[InlineKeyboardButton("Назад", callback_data="back")]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(
            text="Здесь можно решить задачу...", reply_markup=reply_markup
        )

    elif query.data == "back":
        keyboard = [
            [InlineKeyboardButton("Информация", callback_data="info")],
            [InlineKeyboardButton("Теоремы", callback_data="theorems")],
            [InlineKeyboardButton("Шпаргалки", callback_data="cheatsheets")],
            [InlineKeyboardButton("Решить задачу", callback_data="solve")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(
            text="Привет! Я бот калькулятор. Выберите одну из опций:",
            reply_markup=reply_markup,
        )


# Добавляем обработчики команд
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
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))


# Запуск бота
app.run_polling()
