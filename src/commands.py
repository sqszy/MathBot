import os
from telegram import Update, constants
from telegram.ext import ContextTypes
from telegram.helpers import escape_markdown
from handlers.keyboards import get_back_button, get_feedback_keyboard, get_main_keyboard


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f"Привет, {update.effective_user.first_name}! Я твой бот-помощник по математике и могу помочь тебе решить задачу.\n\n "
        "Выбери одну из опций ниже:\n"
        "1. **Посмотреть теоремы и шпаргалки** — воспользуйся полезными материалами для обучения.\n"
        "2. **Отправить изображение или ссылку на изображение** — я извлеку формулу и помогу решить задачу.\n"
        "3. **Отправить текстовую задачу** — напиши формулу, и я решу её.\n"
        "4. **Узнать обо мне информацию** — напиши разработчикам, чтобы изучить как я устроен.",
        parse_mode=constants.ParseMode.MARKDOWN,
        reply_markup=get_main_keyboard()
    )


async def handle_theorems(update: Update, context: ContextTypes.DEFAULT_TYPE):
    theorems = {
        "pi": "[Число Пи - 3,141592...]",
        "trigonometry": "[Информация об Основных тригонометрических тождествах](https://telegra.ph/Osnovnye-trigonometricheskie-tozhdestva-10-11)",
        "derivative": "[Информация о Производных](https://telegra.ph/Proizvodnye-10-11)",
        "tablstep": "[Информация о Таблице степеней](https://telegra.ph/Tablica-stepenej-10-11)",
        "tablsquare": "[Информация о Таблице квадратов](https://telegra.ph/Tablica-kvadratov-10-11)",
        "square": "[Информация о Квадрате](https://telegra.ph/Kvadrat-10-11-3)",
        "rectangle": "[Информация о Прямоугольнике](https://telegra.ph/Pryamougolnik-10-11)",
        "triangle": "[Информация о Треугольнике](https://telegra.ph/Treugolnik-10-11)",
        "rhomb": "[Информация о Ромбе](https://telegra.ph/Romb-10-11)",
        "trapezoid": "[Информация о Трапеции](https://telegra.ph/Trapeciya-10-11)",
        "parallelepiped": "[Информация о Параллелепипеде](https://telegra.ph/Parallelepiped-10-11)",
        "sphere": "[Информация о Сфере](https://telegra.ph/Sfera-10-11)",
        "parallelogram": "[Информация о Параллелограмме](https://telegra.ph/Parallelogramm-10-11)",
        "circle": "[Информация об Окружности](https://telegra.ph/Okruzhnost-10-11)",
        "cone": "[Информация о Конусе](https://telegra.ph/Konus-10-11)",
        "pyramid": "[Информация о Пирамиде](https://telegra.ph/Piramida-10-11-17)",
        "cube": "[Информация о Кубе](https://telegra.ph/Kub-10-11)"
    }
    query = update.callback_query
    if query.data in theorems:
        text = theorems[query.data]
        await query.edit_message_text(
            text=text,
            parse_mode="Markdown",
            reply_markup=get_back_button(callback_data="theorems"),
        )


async def send_cheatsheet(update: Update, file_path: str, caption: str):
    if os.path.exists(file_path):
        with open(file_path, "rb") as file:
            await update.effective_chat.send_document(document=file, caption=caption)
    else:
        await update.effective_chat.send_message(text="Файл не найден!")


async def handle_model_response(update: Update, context: ContextTypes.DEFAULT_TYPE, result: str):
    feedback_message = f"{result}\n\nПонравился ответ?"
    escaped_result = escape_markdown(feedback_message, version=2)
    sent_message = await update.message.reply_text(
        escaped_result,
        parse_mode=constants.ParseMode.MARKDOWN_V2,
        reply_markup=get_feedback_keyboard()
    )
