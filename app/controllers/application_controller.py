from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.schemas.application_schema import (
    LoanApplicationCreate,
    LoanApplicationRead
)
from app.services.application_service import LoanApplicationService
from app.core.database import get_db

router = APIRouter(prefix="/applications", tags=["Loan Applications"])


@router.post(
    "/",
    response_model=LoanApplicationRead,
    status_code=status.HTTP_201_CREATED
)
def apply_for_loan(
    data: LoanApplicationCreate,
    db: Session = Depends(get_db)
):
    service = LoanApplicationService(db)
    try:
        return service.apply_for_loan(
            user_id=data.user_id,
            product_id=data.product_id,
            amount=data.amount
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list[LoanApplicationRead])
def list_applications(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100),
    db: Session = Depends(get_db)
):
    service = LoanApplicationService(db)
    return service.application_repo.list(skip=skip, limit=limit)