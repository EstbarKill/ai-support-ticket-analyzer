from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.services.dashboard_service import DashboardService

router = APIRouter()


@router.get("/summary")
def get_summary(
    db: Session = Depends(get_db)
):

    service = DashboardService(db)

    return service.summary()