from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    ticket_id: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    customer_name: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    customer_email: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    customer_age: Mapped[int | None] = mapped_column(
        nullable=True
    )

    customer_gender: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    product_purchased: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    ticket_type: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    ticket_subject: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    ticket_description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    ticket_status: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    ticket_priority: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    ticket_channel: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )