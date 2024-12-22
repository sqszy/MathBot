import os
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_NAME = os.getenv("BOT_NAME")
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
DB_URL = os.getenv("DB_URL")
