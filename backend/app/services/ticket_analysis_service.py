from app.ai.provider_factory import get_provider

from app.models.ticket_analysis import ( TicketAnalysis )

from app.repositories.ticket_analysis_repository import (
    TicketAnalysisRepository
)


class TicketAnalysisService:

    def __init__(self, db):

        self.db = db

        self.provider = get_provider()

        self.repository = (
            TicketAnalysisRepository(db)
        )

    def analyze_ticket(self, ticket):

        result = self.provider.analyze_ticket(
            ticket.ticket_subject,
            ticket.ticket_description
        )

        analysis = TicketAnalysis(
            ticket_id=ticket.id,
            ai_category=result["category"],
            ai_priority=result["priority"],
            ai_summary=result["summary"],
            ai_sentiment=result["sentiment"],
            ai_team=result["team"],
        )

        self.repository.create(
            analysis
        )

        return analysis

    def commit(self):

        self.repository.commit()