from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from database.database import async_session
from database.crud import get_all_cheatsheets


def get_main_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Шпаргалки", callback_data="cheatsheets"),
         InlineKeyboardButton("Теоремы", callback_data="theorems")],
        [InlineKeyboardButton("Информация", callback_data="info")]
    ])


def get_theorems_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
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
        [InlineKeyboardButton("Назад", callback_data="back")],
    ])


async def get_cheatsheets_keyboard() -> InlineKeyboardMarkup:
    async with async_session() as session:
        cheatsheets = await get_all_cheatsheets(session)
        keyboard = []
        row = []
        for cheatsheet in cheatsheets:
            row.append(
                InlineKeyboardButton(
                    cheatsheet.name, callback_data=cheatsheet.callback_data
                )
            )
            if len(row) == 2:
                keyboard.append(row)
                row = []
        if row:
            keyboard.append(row)
        keyboard.append([InlineKeyboardButton("Назад", callback_data="back")])
        return InlineKeyboardMarkup(keyboard)


def get_back_button(callback_data: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[InlineKeyboardButton("Назад", callback_data=callback_data)]])


def get_feedback_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("👍", callback_data="feedback_yes"),
         InlineKeyboardButton("👎", callback_data="feedback_no")]
    ])
