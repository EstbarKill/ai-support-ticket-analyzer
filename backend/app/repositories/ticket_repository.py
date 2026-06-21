from sqlalchemy.orm import Session

from app.models.ticket import Ticket

from sqlalchemy import exists

from app.models.ticket_analysis import TicketAnalysis

class TicketRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, ticket: Ticket):

        self.db.add(ticket)

    def commit(self):

        self.db.commit()

    def count(self):

        return self.db.query(Ticket).count()

    def delete_all(self):
        self.db.query(Ticket).delete()
        self.db.commit()

    def get_all(self):
        return self.db.query(Ticket).all()

    def get_by_id(self, ticket_id: int):
        return (
            self.db.query(Ticket)
            .filter(Ticket.id == ticket_id)
            .first()
        )
    def get_not_analyzed(
        self,
        limit: int = 4
    ):
        return (
            self.db.query(Ticket)
            .filter(
                ~exists().where(
                    TicketAnalysis.ticket_id == Ticket.id
                )
            )
            .limit(limit)
            .all()
        )