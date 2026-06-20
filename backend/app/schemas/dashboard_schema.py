from pydantic import BaseModel


class DashboardSummary(BaseModel):
    total_tickets: int
    open_tickets: int
    closed_tickets: int
    pending_tickets: int

    critical_tickets: int
    high_tickets: int
    medium_tickets: int
    low_tickets: int