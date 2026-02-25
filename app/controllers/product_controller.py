from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.product_schema import ProductCreate, ProductRead
from app.services.product_service import LoanProductService
from app.core.database import get_db

router = APIRouter(prefix="/products", tags=["Loan Products"])


@router.post(
    "/",
    response_model=ProductRead,
    status_code=status.HTTP_201_CREATED
)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    service = LoanProductService(db)
    try:
        return service.create_product(
            name=product.name,
            interest_rate=product.interest_rate,
            max_amount=product.max_amount
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list[ProductRead])
def list_products(db: Session = Depends(get_db)):
    service = LoanProductService(db)
    return service.list_products()