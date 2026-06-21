import json
import re

import google.generativeai as genai

from app.ai.llm_provider import LLMProvider
from app.config.settings import settings
from google.api_core.exceptions import ResourceExhausted


class GeminiProvider(LLMProvider):

    def __init__(self):

        genai.configure(
            api_key=settings.GEMINI_API_KEY
        )

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )
        
    def generate(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text

    def extract_json(
        self,
        text: str
    ):

        match = re.search(
            r"```json\s*(.*?)\s*```",
            text,
            re.DOTALL
        )

        if match:
            return match.group(1)

        return text

    def analyze_ticket(
        self,
        subject,
        description
    ):

        prompt = f"""
        
        """

        try:

            response = self.model.generate_content(
                prompt
            )

            clean_json = self.extract_json(
                response.text
            )

            return json.loads(
                clean_json
            )

        except ResourceExhausted:

            print(
                "Gemini quota exceeded. Using fallback."
            )

            return {
                "category": "Unknown",
                "priority": "Medium",
                "summary": "Gemini quota exceeded",
                "sentiment": "Neutral",
                "team": "Technical Support"
            }

        except Exception as e:

            return {
                "category": "Unknown",
                "priority": "Medium",
                "summary": str(e),
                "sentiment": "Neutral",
                "team": "Technical Support"
            }