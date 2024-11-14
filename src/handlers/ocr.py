import logging
import re
from telegram import Update, constants
from config.config import TOGETHER_API_KEY
from telegram.ext import ContextTypes
from core.ocr.service import OCRProcessor
from telegram.helpers import escape_markdown

logger = logging.getLogger(__name__)
ocr_processor = OCRProcessor(api_key=TOGETHER_API_KEY)


async def image_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Обработчик изображений и ссылок, отправленных пользователем.
    """
    if update.message.photo:
        # Если сообщение содержит фотографию
        photo_file = await update.message.photo[-1].get_file()
        file_path = await photo_file.download_to_drive()
        logger.info(f"Downloaded photo to {file_path}")
    elif update.message.text and ocr_processor.is_remote_file(update.message.text):
        # Если сообщение содержит ссылку
        file_path = update.message.text
        logger.info(f"Received image URL: {file_path}")
    else:
        # Если сообщение не содержит изображения или ссылки
        await update.message.reply_text(
            "Пожалуйста, отправьте изображение или ссылку на изображение.",
            parse_mode=constants.ParseMode.MARKDOWN_V2,
        )
        return

    try:
        # Выполняем OCR для извлечения текста
        result = await ocr_processor.ocr(file_path, model="Llama-3.2-11B-Vision")

        # Ищем LaTeX-формулу в тексте
        formula_match = re.search(
            r"(?<!\\)(\$.+?\$|\\$begin:math:display$.+?\\\\$end:math:display$|\\$begin:math:text$.*?\\\\$end:math:text$)",
            result
        )

        if formula_match:
            formula = formula_match.group(0).strip()

            # Экранируем формулу (только обратные апострофы внутри формулы)
            escaped_formula = formula.replace('`', '\\`')

            # Экранируем тройные обратные апострофы
            code_block = f"\\`\\`\\`\n{escaped_formula}\n\\`\\`\\`"

            # Отправляем объяснение перед формулой
            explanation_text = "Извлеченная формула из изображения представлена ниже:"
            await update.message.reply_text(
                escape_markdown(explanation_text, version=2),
                parse_mode=constants.ParseMode.MARKDOWN_V2,
            )

            # Отправляем саму формулу в кодовом блоке
            await update.message.reply_text(
                code_block,
                parse_mode=constants.ParseMode.MARKDOWN_V2,
            )

            # Дополнительное объяснение формулы
            additional_info = (
                "Данная формула используется для решения уравнений, включающих переменные и коэффициенты."
            )
            await update.message.reply_text(
                escape_markdown(additional_info, version=2),
                parse_mode=constants.ParseMode.MARKDOWN_V2,
            )
        else:
            # Если формула не найдена, отправляем весь результат
            await update.message.reply_text(
                escape_markdown(result, version=2),
                parse_mode=constants.ParseMode.MARKDOWN_V2,
            )
    except Exception as e:
        # Обработка ошибок
        logger.error(f"Error processing image: {e}")
        await update.message.reply_text(
            "Произошла ошибка при обработке изображения. Попробуйте снова.",
            parse_mode=constants.ParseMode.MARKDOWN_V2,
        )
