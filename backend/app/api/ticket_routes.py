from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.schemas.ticket_schema import TicketResponse

from app.repositories.ticket_repository import TicketRepository

from app.services.csv_import_service import CSVImportService

router = APIRouter()

## Listar tickets ##
@router.get(
    "",
    response_model=list[TicketResponse]
)
def get_tickets(
    db: Session = Depends(get_db)
):

    repository = TicketRepository(db)

    return repository.get_all()

## Obtener ticket por id ##

@router.get(
    "/{ticket_id}",
    response_model=TicketResponse
)
def get_ticket(
    ticket_id: int,
    db: Session = Depends(get_db)
):

    repository = TicketRepository(db)

    return repository.get_by_id(ticket_id)

## Importar datos ##
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