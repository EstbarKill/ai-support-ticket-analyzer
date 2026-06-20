from app.database.session import engine

from app.models.base import Base

from app.models.ticket import Ticket

from app.models.ticket_analysis import TicketAnalysis

def init_db():
    Base.metadata.create_all(bind=engine)