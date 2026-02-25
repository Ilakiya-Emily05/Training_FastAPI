from sqlalchemy.orm import Session
from app.models.loan_product import LoanProduct

class LoanProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, product_id: int) -> LoanProduct | None:
        return self.db.query(LoanProduct).filter(
            LoanProduct.id == product_id
        ).first()

    def create(self, product: LoanProduct) -> LoanProduct:
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def list(self) -> list[LoanProduct]:
        return self.db.query(LoanProduct).all()