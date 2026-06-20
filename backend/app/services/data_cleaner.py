import re


class DataCleaner:

    PRIORITY_MAP = {
        "critical": "Critical",
        "urgent": "Critical",
        "p1": "Critical",

        "high": "High",
        "p2": "High",

        "medium": "Medium",
        "p3": "Medium",

        "low": "Low",
        "p4": "Low",
    }

    @staticmethod
    def clean_text(value):

        if value is None:
            return None

        value = str(value).strip()

        if value == "":
            return None

        return value

    @staticmethod
    def clean_email(email):

        if not email:
            return None

        return str(email).strip().lower()

    @staticmethod
    def normalize_priority(priority):

        if not priority:
            return "Medium"

        value = str(priority).strip().lower()

        return DataCleaner.PRIORITY_MAP.get(
            value,
            "Medium"
        )

    @staticmethod
    def is_valid_email(email):

        if not email:
            return False

        pattern = r"^[^@]+@[^@]+\.[^@]+$"

        return bool(
            re.match(pattern, email)
        )