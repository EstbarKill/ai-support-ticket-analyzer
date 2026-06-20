from sqlalchemy.orm import Session

from app.models.ticket_analysis import TicketAnalysis


class TicketAnalysisRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, analysis):

        self.db.add(analysis)

    def commit(self):

        self.db.commit()

    def delete_all(self):

        self.db.query(
            TicketAnalysis
        ).delete()

        self.db.commit()