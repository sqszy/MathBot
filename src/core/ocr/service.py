import base64
import os
from typing import Optional
import logging
from together import AsyncTogether as Together


class OCRProcessor:
    def __init__(self, api_key: Optional[str], logger: Optional[logging.Logger] = None):
        """
        Инициализация OCRProcessor.
        :param api_key: Ключ API Together.
        :param logger: Логгер для записи событий (по умолчанию используется root-логгер).
        """
        self.api_key = api_key
        self.logger = logger or logging.getLogger(__name__)
        self.client = Together(api_key=self.api_key)
        self.logger.debug("Together client initialized")

    async def ocr(self, file_path: str, model: str = "free") -> str:
        """
        Основная функция для выполнения OCR.
        :param file_path: Путь к файлу (локальный или URL).
        :param model: Название модели ("Llama-3.2-90B-Vision", "Llama-3.2-11B-Vision", "free").
        :return: Markdown текст, полученный из изображения.
        """
        vision_llm = (
            "meta-llama/Llama-Vision-Free"
            if model == "free"
            else f"meta-llama/{model}-Instruct-Turbo"
        )
        self.logger.info(f"Using model: {vision_llm}")

        final_markdown = await self._get_markdown(
            together=self.client, vision_llm=vision_llm, file_path=file_path
        )

        return final_markdown

    async def _get_markdown(self, together: Together, vision_llm: str, file_path: str) -> str:
        """
        Генерирует Markdown из изображения.
        :param together: Клиент Together.
        :param vision_llm: Название модели.
        :param file_path: Путь к изображению.
        :return: Markdown текст.
        """
        system_prompt = (
            "Extract the mathematical formula from the provided image and convert it into LaTeX format. "
            "The result should be returned as a LaTeX-compatible string without any additional explanations.\n\n"
            "For example:\n"
            "Image: A quadratic formula.\n"
            "Result: x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}\n\n"
            "Please ensure that mathematical notations are accurately represented.\n\n"
            "Provide response in Russian language to explain the formula")

        # Подготовка изображения
        final_image_url = (
            file_path
            if self.is_remote_file(file_path)
            else f"data:image/jpeg;base64,{self._encode_image(file_path)}"
        )
        self.logger.debug(f"Final image URL: {final_image_url[:100]}...")

        try:
            output = await together.chat.completions.create(
                model=vision_llm,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": system_prompt},
                            {"type": "image_url", "image_url": {"url": final_image_url}},
                        ],
                    }
                ],
            )
            self.logger.debug(f"API response: {output}")
            if not output.choices[0].message.content:
                self.logger.warning("API returned empty content.")
                raise ValueError("Empty content in API response.")
            return output.choices[0].message.content
        except Exception as e:
            self.logger.error(f"Error during API call: {e}")
            raise

    def _encode_image(self, image_path: str) -> str:
        """
        Кодирует изображение в строку Base64.
        :param image_path: Путь к локальному файлу изображения.
        :return: Строка Base64.
        """
        if not os.path.exists(image_path):
            self.logger.error(f"File not found: {image_path}")
            raise FileNotFoundError(f"File not found: {image_path}")

        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
            self.logger.debug("Image encoded to Base64")
            return encoded_string

    def is_remote_file(self, file_path: str) -> bool:
        """
        Проверяет, является ли путь к файлу удаленным (URL).
        :param file_path: Путь к файлу.
        :return: True, если файл удаленный (URL), иначе False.
        """
        return file_path.startswith("http://") or file_path.startswith("https://")
