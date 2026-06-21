# app/services/data_quality_service.py

from collections import Counter

from app.services.data_cleaner import DataCleaner


class DataQualityService:

    VALID_PRIORITIES = {
        "Low",
        "Medium",
        "High",
        "Critical"
    }

    def analyze(self, tickets):

        report = {
            "total_tickets": 0,
            "invalid_emails": 0,
            "missing_values": 0,
            "invalid_priorities": 0,
            "duplicate_tickets": 0,
            "invalid_dates": 0
        }

        ticket_ids = []

        for ticket in tickets:

            report["total_tickets"] += 1

            # -------------------------
            # Duplicate Tickets
            # -------------------------

            ticket_id = getattr(
                ticket,
                "ticket_id",
                None
            )

            if ticket_id:
                ticket_ids.append(ticket_id)

            # -------------------------
            # Email Validation
            # -------------------------

            email = getattr(
                ticket,
                "customer_email",
                None
            )

            if email and not DataCleaner.is_valid_email(email):
                report["invalid_emails"] += 1

            # -------------------------
            # Priority Validation
            # -------------------------

            priority = getattr(
                ticket,
                "priority",
                None
            )

            if priority:

                normalized = DataCleaner.normalize_priority(
                    priority
                )

                if normalized not in self.VALID_PRIORITIES:
                    report["invalid_priorities"] += 1

            # -------------------------
            # Missing Values
            # -------------------------

            for value in vars(ticket).values():

                if DataCleaner.is_missing(value):
                    report["missing_values"] += 1

            # -------------------------
            # Date Validation
            # -------------------------

            created_at = getattr(
                ticket,
                "created_at",
                None
            )

            if created_at:

                if not DataCleaner.is_valid_date(
                    created_at
                ):
                    report["invalid_dates"] += 1

        # -------------------------
        # Duplicate Count
        # -------------------------

        duplicates = 0

        counter = Counter(ticket_ids)

        for count in counter.values():

            if count > 1:
                duplicates += count - 1

        report["duplicate_tickets"] = duplicates

        return report