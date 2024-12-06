import base64
import os
from typing import Optional, List, Dict
import logging
from together import AsyncTogether as Together


class AIProcessor:
    def __init__(self, api_key: Optional[str], logger: Optional[logging.Logger] = None):
        """
        Инициализация AIProcessor.
        :param api_key: Ключ API Together.
        :param logger: Логгер для записи событий (по умолчанию используется root-логгер).
        """
        self.api_key = api_key
        self.logger = logger or logging.getLogger(__name__)
        self.client = Together(api_key=self.api_key)
        self.logger.debug("Together client initialized")

    async def extract_formula_from_image(self, file_path: str, model: str = "free") -> str:
        """
        Извлекает математическую формулу из изображения.
        :param file_path: Путь к файлу (локальный или URL).
        :param model: Название модели ("Llama-3.2-90B-Vision", "Llama-3.2-11B-Vision", "free").
        :return: Извлечённая формула в виде текста.
        """
        self.logger.info(f"Using model: {model}")
        system_prompt = (
            "Извлеките математическую формулу из предоставленного изображения и представьте её в упрощённом текстовом формате, "
            "используя такие символы, как '+', '-', 'sqrt()', '/', '_()' и '^()' для квадратных корней, деления и степеней соответственно. "
            "Не включайте никаких дополнительных объяснений или шагов.")
        final_image_url = (
            file_path
            if self.is_remote_file(file_path)
            else f"data:image/jpeg;base64,{self._encode_image(file_path)}"
        )
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": system_prompt},
                    {"type": "image_url", "image_url": {"url": final_image_url}},
                ],
            }
        ]

        formula_text = await self._get_response(messages=messages, model=model)
        self.logger.info(formula_text.strip())
        return formula_text.strip()

    async def solve_problem(self, formula_text: str, model: str = "free") -> str:
        """
        Решает математическую задачу, используя формулу.
        :param formula_text: Формула, извлечённая из изображения.
        :param model: Название модели.
        :return: Шаги решения и окончательный ответ.
        """
        self.logger.info(f"Using model: {model}")
        system_prompt = (
            f"Пожалуйста, решите следующую математическую формулу: {formula_text}. "
            "Сначала выведите формулу. Предоставьте решение в нескольких коротких шагах и конечный ответ. Не пиши очень много."
        )
        messages = [
            {
                "role": "user",
                "content": system_prompt,
            }
        ]
        solution = await self._get_response(messages=messages, model=model)
        return solution.strip()

    async def _get_response(self, messages: List[Dict], model: str) -> str:
        """
        Отправляет сообщения в API Together и возвращает ответ.
        :param messages: Список сообщений для отправки.
        :param model: Модель для использования.
        :return: Ответ ИИ.
        """
        try:
            output = await self.client.chat.completions.create(
                model=model,
                messages=messages,
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
        file_path = str(file_path)
        return file_path.startswith("http://") or file_path.startswith("https://")
