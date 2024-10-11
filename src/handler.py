from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ContextTypes,
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
