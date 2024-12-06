import logging
from commands import handle_model_response
from telegram import Update, constants
from telegram.ext import ContextTypes
from config.config import TOGETHER_API_KEY
from core.ocr.service import AIProcessor
from handlers.keyboards import get_back_button


logger = logging.getLogger(__name__)
ai_processor = AIProcessor(api_key=TOGETHER_API_KEY)


async def ai_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Обработчик изображений, ссылок и текстовых сообщений, отправленных пользователем.
    """
    if update.message.photo:
        # Если сообщение содержит фотографию
        photo_file = await update.message.photo[-1].get_file()
        file_path = await photo_file.download_to_drive()
        logger.info(f"Downloaded photo to {file_path}")
        context.user_data["last_photo"] = file_path
        try:
            sent_message = await update.message.reply_text(text="Думаю...")
            formula = await ai_processor.extract_formula_from_image(file_path, model="meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo")
            await sent_message.edit_text(text="Решаю...")
            result = await ai_processor.solve_problem(formula, model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo")
            await sent_message.delete()
            await handle_model_response(update, context, result)
        except Exception as e:
            logger.error(f"Error processing image: {e}")
            await update.message.reply_text(
                "Произошла ошибка при обработке изображения. Попробуйте снова.",
                parse_mode=constants.ParseMode.MARKDOWN_V2,
                reply_markup=get_back_button(callback_data="back")
            )
    elif update.message.text:
        # Если сообщение содержит текст
        user_text = update.message.text.strip()
        context.user_data["last_text"] = user_text
        try:
            sent_message = await update.message.reply_text(text="Думаю...")
            if ai_processor.is_remote_file(user_text):
                # Если это ссылка
                logger.info(f"Received image URL: {user_text}")
                formula = await ai_processor.extract_formula_from_image(user_text, model="meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo")
            else:
                # Если это просто текст
                formula = user_text
            await sent_message.edit_text(text="Решаю...")
            result = await ai_processor.solve_problem(formula, model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo")
            await sent_message.delete()
            await handle_model_response(update, context, result)
        except Exception as e:
            logger.error(f"Error processing text or URL: {e}")
            await update.message.reply_text(
                "Произошла ошибка при обработке вашего текста. Попробуйте снова.",
                reply_markup=get_back_button(callback_data="back")
            )
    else:
        await update.message.reply_text(
            "Пожалуйста, отправьте изображение, ссылку на изображение или текст.",
            reply_markup=get_back_button(callback_data="back")
        )
