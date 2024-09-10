import os

from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.env'))


# Загружаем переменные окружения из .env файла
class Settings:
    INSTAGRAM_API_URL = "https://graph.facebook.com/v12.0/me/messages"
    CLIENT_ID = os.environ.get("CLIENT_ID")
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
    REDIRECT_URI = os.environ.get("REDIRECT_URI")
    ACCESS_TOKEN_URL = os.environ.get("ACCESS_TOKEN_URL")
    LONG_LIVED_TOKEN_URL = os.environ.get("LONG_LIVED_TOKEN_URL")


settings = Settings()
