from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.repayment_schema import RepaymentCreate, RepaymentRead
from app.services.repayment_service import RepaymentService
from app.core.database import get_db

router = APIRouter(prefix="/repayments", tags=["Repayments"])


@router.post(
    "/",
    response_model=RepaymentRead,
    status_code=status.HTTP_201_CREATED
)
def make_repayment(
    data: RepaymentCreate,
    db: Session = Depends(get_db)
):
    service = RepaymentService(db)
    try:
        return service.make_repayment(
            application_id=data.application_id,
            amount=data.amount
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))