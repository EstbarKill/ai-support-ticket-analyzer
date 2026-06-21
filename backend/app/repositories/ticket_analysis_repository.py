from sqlalchemy.orm import Session

from app.models.ticket_analysis import (
    TicketAnalysis
)


class TicketAnalysisRepository:

    def __init__(
        self,
        db: Session
    ):
        self.db = db

    def create(
        self,
        analysis
    ):
        self.db.add(
            analysis
        )

    def commit(self):
        self.db.commit()

    def delete_all(self):

        self.db.query(
            TicketAnalysis
        ).delete()

        self.db.commit()

    def exists_for_ticket(
        self,
        ticket_id: int
    ):

        return (
            self.db.query(
                TicketAnalysis
            )
            .filter(
                TicketAnalysis.ticket_id == ticket_id
            )
            .first()
            is not None
        )

    def get_all(self):

        return (
            self.db.query(
                TicketAnalysis
            )
            .all()
        )