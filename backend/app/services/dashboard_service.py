from sqlalchemy.orm import Session

from app.models.ticket import Ticket


class DashboardService:

    def __init__(self, db: Session):
        self.db = db

    def summary(self):

        total = self.db.query(Ticket).count()

        open_tickets = (
            self.db.query(Ticket)
            .filter(Ticket.ticket_status == "Open")
            .count()
        )

        closed_tickets = (
            self.db.query(Ticket)
            .filter(Ticket.ticket_status == "Closed")
            .count()
        )

        pending_tickets = (
            self.db.query(Ticket)
            .filter(
                Ticket.ticket_status ==
                "Pending Customer Response"
            )
            .count()
        )

        critical = (
            self.db.query(Ticket)
            .filter(
                Ticket.ticket_priority == "Critical"
            )
            .count()
        )

        high = (
            self.db.query(Ticket)
            .filter(
                Ticket.ticket_priority == "High"
            )
            .count()
        )

        medium = (
            self.db.query(Ticket)
            .filter(
                Ticket.ticket_priority == "Medium"
            )
            .count()
        )

        low = (
            self.db.query(Ticket)
            .filter(
                Ticket.ticket_priority == "Low"
            )
            .count()
        )

        return {
            "total_tickets": total,
            "open_tickets": open_tickets,
            "closed_tickets": closed_tickets,
            "pending_tickets": pending_tickets,
            "critical_tickets": critical,
            "high_tickets": high,
            "medium_tickets": medium,
            "low_tickets": low,
        }