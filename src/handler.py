from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from src.commands import (
    pi,
    trigonometry,
    derivative,
    tablstep,
    tablsquare,
    square,
    rectangle,
    triangle,
    rhomb,
    trapezoid,
    parallelepiped,
    sphere,
    parallelogram,
    circle,
    cone,
    pyramid,
    cube,
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
        keyboard = [
            [InlineKeyboardButton("Число Пи", callback_data="pi"),
             InlineKeyboardButton("Тригонометрия", callback_data="trigonometry")],
            [InlineKeyboardButton("Производные", callback_data="derivative"),
             InlineKeyboardButton("Таблица степеней", callback_data="tablstep")],
            [InlineKeyboardButton("Таблица квадратов", callback_data="tablsquare"),
             InlineKeyboardButton("Квадрат", callback_data="square")],
            [InlineKeyboardButton("Прямоугольник", callback_data="rectangle"),
             InlineKeyboardButton("Треугольник", callback_data="triangle")],
            [InlineKeyboardButton("Ромб", callback_data="rhomb"),
             InlineKeyboardButton("Трапеция", callback_data="trapezoid")],
            [InlineKeyboardButton("Параллелепипед", callback_data="parallelepiped"),
             InlineKeyboardButton("Сфера", callback_data="sphere")],
            [InlineKeyboardButton("Параллелограмм", callback_data="parallelogram"),
             InlineKeyboardButton("Окружность", callback_data="circle")],
            [InlineKeyboardButton("Конус", callback_data="cone"),
             InlineKeyboardButton("Пирамида", callback_data="pyramid")],
            [InlineKeyboardButton("Куб", callback_data="cube")],
            [InlineKeyboardButton("Назад", callback_data="back")]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(
            text="Выберите теорему:", reply_markup=reply_markup
        )

    elif query.data == "back":
        keyboard = [
            [InlineKeyboardButton("Информация", callback_data="info"),
             InlineKeyboardButton("Теоремы", callback_data="theorems")],
            [InlineKeyboardButton("Шпаргалки", callback_data="cheatsheets"),
             InlineKeyboardButton("Решить задачу", callback_data="solve")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text="Привет! Я бот-помощник по математике и другим предметам. Выберите одну из опций:",
            reply_markup=reply_markup,
        )
    elif query.data in ["pi", "trigonometry", "derivative", "tablstep", "tablsquare",
                        "square", "rectangle", "triangle", "rhomb", "trapezoid",
                        "parallelepiped", "sphere", "parallelogram", "circle",
                        "cone", "pyramid", "cube"]:
        await handle_theorems(query, context)


async def handle_theorems(query, context: ContextTypes.DEFAULT_TYPE):
    theorems = {
        "pi": pi,
        "trigonometry": trigonometry,
        "derivative": derivative,
        "tablstep": tablstep,
        "tablsquare": tablsquare,
        "square": square,
        "rectangle": rectangle,
        "triangle": triangle,
        "rhomb": rhomb,
        "trapezoid": trapezoid,
        "parallelepiped": parallelepiped,
        "sphere": sphere,
        "parallelogram": parallelogram,
        "circle": circle,
        "cone": cone,
        "pyramid": pyramid,
        "cube": cube,
    }

    if query.data in theorems:
        await theorems[query.data](query, context)
