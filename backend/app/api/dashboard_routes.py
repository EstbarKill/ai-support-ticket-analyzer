from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.services.dashboard_service import DashboardService
from app.repositories.ticket_repository import TicketRepository

from app.services.data_quality_service import DataQualityService

router = APIRouter()

from app.schemas.data_quality_response import (
    DataQualityResponse
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get(
    "/data-quality",
    response_model=DataQualityResponse
)
def get_data_quality(
    db: Session = Depends(get_db)
):

    repository = TicketRepository(db)

    tickets = repository.get_all()

    quality_service = DataQualityService()

    report = quality_service.analyze(
        tickets
    )

    return report
    
@router.get("/summary")
def get_summary(
    db: Session = Depends(get_db)
):

    service = DashboardService(db)

    return service.summary()