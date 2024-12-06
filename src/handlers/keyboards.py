from telegram import InlineKeyboardButton, InlineKeyboardMarkup


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


def get_cheatsheets_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Вся школьная программа", callback_data="cheatsheet_1"),
         InlineKeyboardButton("Дискретная математика", callback_data="cheatsheet_2")],
        [InlineKeyboardButton("Линейная алгебра", callback_data="cheatsheet_3"),
         InlineKeyboardButton("Математический анализ", callback_data="cheatsheet_4")],
        [InlineKeyboardButton("Назад", callback_data="back")]
    ])


def get_back_button(callback_data: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[InlineKeyboardButton("Назад", callback_data=callback_data)]])


def get_feedback_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("👍", callback_data="feedback_yes"),
         InlineKeyboardButton("👎", callback_data="feedback_no")]
    ])
