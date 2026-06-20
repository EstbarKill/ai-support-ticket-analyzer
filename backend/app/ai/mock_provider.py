from app.ai.llm_provider import LLMProvider


class MockProvider(LLMProvider):

    def analyze_ticket(
        self,
        subject,
        description
    ):

        return {
            "category": "Technical Issue",
            "priority": "Medium",
            "summary": (
                description[:150]
                if description
                else "No description"
            ),
            "sentiment": "Neutral",
            "team": "Technical Support"
        }