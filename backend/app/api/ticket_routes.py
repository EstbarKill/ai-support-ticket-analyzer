from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.repositories.ticket_repository import TicketRepository

from app.services.csv_import_service import CSVImportService

router = APIRouter()

@router.post("/import")
def import_tickets(
    db: Session = Depends(get_db)
):

    repository = TicketRepository(db)

    repository.delete_all()

    service = CSVImportService()

    tickets = service.load()

    for ticket in tickets:
        repository.create(ticket)

    repository.commit()

    return {
        "imported": len(tickets)
    }