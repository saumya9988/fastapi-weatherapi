import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENWEATHERMAP_API_KEY: str = os.getenv("WEATHER_API_KEY")

settings = Settings()