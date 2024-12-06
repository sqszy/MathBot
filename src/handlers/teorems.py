import logging
from telegram import Update, constants
from telegram.ext import ContextTypes
from telegram.helpers import escape_markdown
from handlers.keyboards import get_back_button, get_cheatsheets_keyboard, get_feedback_keyboard, get_main_keyboard, get_theorems_keyboard
from commands import handle_model_response, handle_theorems, send_cheatsheet
from core.ocr.service import AIProcessor
from config.config import TOGETHER_API_KEY

logger = logging.getLogger(__name__)
ai_processor = AIProcessor(api_key=TOGETHER_API_KEY)


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == "info":
        await query.edit_message_text(
            text="Привет! Мы студенты 3 курса. Мы создали бота-помощника по математике на языке Python. Это курсовая работа по предмету - Технология программирования.  Если хочешь узнать как реализован бот, или есть какие-то технические неполадки, то напиши нам: [@jjkxxd](https://t.me/jjkxxd), [@mark_danko](https://t.me/mark_danko).",
            parse_mode="Markdown",
            reply_markup=get_back_button(callback_data="back")
        )
    elif query.data == "theorems":
        await query.edit_message_text(
            text="Выберите одну из фигур для изучения информации:", reply_markup=get_theorems_keyboard()
        )
    elif query.data == "cheatsheets":
        await query.edit_message_text(
            text="Выберите шпаргалку:", reply_markup=get_cheatsheets_keyboard()
        )
    elif query.data.startswith("cheatsheet_"):
        file_map = {
            "cheatsheet_1": ("src/files/allsch.pdf", "Вся школьная программа в 1 файле:"),
            "cheatsheet_2": ("src/files/discret.pdf", "Дискретная математика в 1 файле:"),
            "cheatsheet_3": ("src/files/linal.pdf", "Линейная алгебра в 1 файле:"),
            "cheatsheet_4": ("src/files/mathan.pdf", "Математический анализ в 1 файле:")
        }
        file_path, caption = file_map.get(query.data)
        await send_cheatsheet(update, file_path, caption)
    elif query.data == "feedback_yes":
        await query.message.reply_text(
            "Спасибо, что выбрали меня! Выберите одну из опций или отправьте изображение, ссылку или текст и я помогу ее решить.",
            reply_markup=get_main_keyboard()
        )
    elif query.data == "feedback_no":
        await query.delete_message()
        if "last_photo" in context.user_data:
            file_path = context.user_data["last_photo"]
            sent_message = await query.message.reply_text(text="Думаю...")
            try:
                formula = await ai_processor.extract_formula_from_image(file_path, model="meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo")
                await sent_message.edit_text(text="Решаю...")
                result = await ai_processor.solve_problem(formula, model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo")
                await sent_message.delete()
                context.user_data["last_formula"] = formula
                await handle_model_response(query, context, result)
            except Exception as e:
                logger.error(f"Error processing image again: {e}")
                await query.message.reply_text(
                    "Произошла ошибка при повторной обработке изображения. Попробуйте снова.",
                    parse_mode=constants.ParseMode.MARKDOWN_V2,
                    reply_markup=get_back_button(callback_data="back")
                )
        elif "last_text" in context.user_data:
            user_text = context.user_data["last_text"]
            sent_message = await query.message.reply_text(text="Думаю...")
            try:
                if ai_processor.is_remote_file(user_text):
                    formula = await ai_processor.extract_formula_from_image(user_text, model="meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo")
                else:
                    formula = user_text
                await sent_message.edit_text(text="Решаю...")
                result = await ai_processor.solve_problem(formula, model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo")
                await sent_message.delete()
                await handle_model_response(query, context, result)
            except Exception as e:
                logger.error(f"Error processing text again: {e}")
                await query.message.reply_text(
                    "Произошла ошибка при повторной обработке вашего текста. Попробуйте снова.",
                    reply_markup=get_back_button(callback_data="back")
                )
        else:
            await query.message.reply_text(
                "К сожалению, у нас нет данных для повторной обработки. Пожалуйста, отправьте изображение, ссылку или текст.",
                reply_markup=get_back_button(callback_data="back")
            )
    elif query.data == "back":
        current_text = query.message.text

        if current_text.startswith("Число Пи") or current_text.startswith("Информация о"):
            await query.edit_message_text(
                text="Выберите одну из фигур для изучения информации:",
                reply_markup=get_theorems_keyboard()
            )
        elif current_text.startswith("Выберите шпаргалку"):
            await query.delete_message()
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Привет! Я твой бот-помощник по математике. Я могу помочь тебе решить задачу. Выберите одну из опций или отправьте изображение, ссылку или текст и я помогу ее решить.",
                reply_markup=get_main_keyboard()
            )
        else:
            await query.edit_message_text(
                text="Привет! Я твой бот-помощник по математике. Я могу помочь тебе решить задачу. Выберите одну из опций или отправьте изображение, ссылку или текст и я помогу ее решить.",
                reply_markup=get_main_keyboard()
            )
    else:
        await handle_theorems(update, context)
