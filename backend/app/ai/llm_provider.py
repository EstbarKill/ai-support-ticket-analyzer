from abc import ABC
from abc import abstractmethod


class LLMProvider(ABC):

    @abstractmethod
    def analyze_ticket(
        self,
        subject: str,
        description: str
    ):
        pass