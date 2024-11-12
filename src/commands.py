from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.callback_query:
        message = update.callback_query.message
    else:
        message = update.message

    keyboard = [
        [InlineKeyboardButton("Информация", callback_data="info"),
         InlineKeyboardButton("Теоремы", callback_data="theorems")],
        [InlineKeyboardButton("Шпаргалки", callback_data="cheatsheets"),
         InlineKeyboardButton("Решить задачу", callback_data="solve")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if message:
        await message.reply_text(
            f"Привет, {update.effective_user.first_name}! Я бот калькулятор, созданный на языке \
                Python. Это курсовая работа по предмету - Технология программирования.",
            reply_markup=reply_markup,
        )


async def pi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.message.chat.id, text="[Число Пи - 3,141592...]"
    )


async def trigonometry(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.message.chat.id,
        text="[Основные тригонометрические тождества]\
            (https://telegra.ph/Osnovnye-trigonometricheskie-tozhdestva-10-11)",
        parse_mode="Markdown",
    )


async def derivative(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.message.chat.id,
        text="[Производные](https://telegra.ph/Proizvodnye-10-11)",
        parse_mode="Markdown",
    )


async def tablstep(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.message.chat.id,
        text="[Таблица степеней](https://telegra.ph/Tablica-stepenej-10-11)",
        parse_mode="Markdown",
    )


async def tablsquare(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.message.chat.id,
        text="[Таблица квадратов](https://telegra.ph/Tablica-kvadratov-10-11)",
        parse_mode="Markdown",
    )


async def square(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.message.chat.id,
        text="[\nКвадрат](https://telegra.ph/Kvadrat-10-11-3)",
        parse_mode="Markdown",
    )


async def rectangle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.message.chat.id,
        text="[\nПрямоугольник](https://telegra.ph/Pryamougolnik-10-11)",
        parse_mode="Markdown",
    )


async def triangle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.message.chat.id,
        text="[\nТреугольник](https://telegra.ph/Treugolnik-10-11)",
        parse_mode="Markdown",
    )


async def rhomb(query, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=query.message.chat.id,
        text="[\nРомб](https://telegra.ph/Romb-10-11)",
        parse_mode="Markdown",
    )


async def trapezoid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.message.chat.id,
        text="[\nТрапеция](https://telegra.ph/Trapeciya-10-11)",
        parse_mode="Markdown",
    )


async def parallelepiped(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.message.chat.id,
        text="[\nПараллелепипед](https://telegra.ph/Parallelepiped-10-11)",
        parse_mode="Markdown",
    )


async def sphere(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.message.chat.id,
        text="[\nСфера](https://telegra.ph/Sfera-10-11)",
        parse_mode="Markdown",
    )


async def parallelogram(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.message.chat.id,
        text="[\nПараллелограмм](https://telegra.ph/Parallelogramm-10-11)",
        parse_mode="Markdown",
    )


async def circle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.message.chat.id,
        text="[\nОкружность](https://telegra.ph/Okruzhnost-10-11)",
        parse_mode="Markdown",
    )


async def cone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.message.chat.id,
        text="[\nКонус](https://telegra.ph/Konus-10-11)",
        parse_mode="Markdown",
    )


async def pyramid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.message.chat.id,
        text="[\nПирамида](https://telegra.ph/Piramida-10-11-17)",
        parse_mode="Markdown",
    )


async def cube(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.message.chat.id,
        text="[\nКуб](https://telegra.ph/Kub-10-11)",
        parse_mode="Markdown",
    )
