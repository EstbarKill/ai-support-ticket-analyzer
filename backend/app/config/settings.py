from dotenv import load_dotenv
import os

load_dotenv()

class Settings:

    GEMINI_API_KEY = os.getenv(
        "GEMINI_API_KEY"
    )

    LLM_PROVIDER = os.getenv(
        "LLM_PROVIDER",
        "mock"
    )

settings = Settings()