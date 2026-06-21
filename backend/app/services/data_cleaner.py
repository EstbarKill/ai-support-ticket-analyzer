import re

from datetime import datetime

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

    STATUS_MAP = {
        "open": "Open",
        "opened": "Open",

        "in progress": "In Progress",
        "in_progress": "In Progress",

        "resolved": "Resolved",

        "closed": "Closed",
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
    def normalize_status(status):

        if not status:
            return "Open"

        value = str(status).strip().lower()

        return DataCleaner.STATUS_MAP.get(
            value,
            "Open"
        )

    @staticmethod
    def is_missing(value):

        if value is None:
            return True

        value = str(value).strip().lower()

        return value in [
            "",
            "null",
            "none",
            "nan",
            "n/a"
        ]

    @staticmethod
    def is_valid_date(value):

        if not value:
            return False

        try:

            datetime.fromisoformat(
                str(value)
            )

            return True

        except Exception:
            return False
        
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