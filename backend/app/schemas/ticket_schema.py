from pydantic import BaseModel
from typing import Optional


class TicketResponse(BaseModel):
    id: int
    ticket_id: Optional[str]
    customer_name: Optional[str]
    customer_email: Optional[str]
    product_purchased: Optional[str]
    ticket_type: Optional[str]
    ticket_subject: Optional[str]
    ticket_status: Optional[str]
    ticket_priority: Optional[str]
    ticket_channel: Optional[str]

    class Config:
        from_attributes = True