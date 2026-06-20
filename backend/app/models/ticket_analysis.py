from datetime import datetime

from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base import Base


class TicketAnalysis(Base):
    __tablename__ = "ticket_analysis"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    ticket_id: Mapped[int] = mapped_column(
        ForeignKey("tickets.id")
    )

    ai_category: Mapped[str | None] = mapped_column(
        String(255)
    )

    ai_priority: Mapped[str | None] = mapped_column(
        String(100)
    )

    ai_summary: Mapped[str | None] = mapped_column(
        Text
    )

    ai_sentiment: Mapped[str | None] = mapped_column(
        String(100)
    )

    ai_team: Mapped[str | None] = mapped_column(
        String(255)
    )

    analyzed_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )