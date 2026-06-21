from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.schemas.ticket_schema import TicketResponse

from app.repositories.ticket_repository import TicketRepository

from app.services.csv_import_service import CSVImportService

from app.services.ticket_analysis_service import ( TicketAnalysisService )

router = APIRouter()

## Realizar analisis##

@router.post("/analyze")
def analyze_tickets(
    db: Session = Depends(get_db)
):

    repository = TicketRepository(db)

    service = TicketAnalysisService(db)

    tickets = repository.get_not_analyzed()

    pending_tickets = []

    processed = 0

    for ticket in tickets:

        result = service.analyze_ticket(
            ticket
        )

    if result:
        processed += 1

    for ticket in pending_tickets:

        result = service.analyze_ticket(
            ticket
        )

        if result:
            processed += 1

    service.commit()

    return {
        "processed": processed
    }

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