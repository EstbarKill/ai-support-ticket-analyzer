from app.database.session import engine

from app.models.base import Base

from app.models.ticket import Ticket


def init_db():
    Base.metadata.create_all(bind=engine)