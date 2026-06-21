from pydantic import BaseModel


class DataQualityResponse(BaseModel):
    total_tickets: int
    invalid_emails: int
    missing_values: int
    invalid_priorities: int
    duplicate_tickets: int
    invalid_dates: int