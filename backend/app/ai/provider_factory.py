from app.config.settings import settings

from app.ai.mock_provider import MockProvider
from app.ai.gemini_provider import GeminiProvider


def get_provider():

    if (
        settings.LLM_PROVIDER.lower()
        == "gemini"
    ):
        return GeminiProvider()

    return MockProvider()