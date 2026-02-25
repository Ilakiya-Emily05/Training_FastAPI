from sqlalchemy.orm import Session
from app.repositories.product_repository import LoanProductRepository
from app.models.loan_product import LoanProduct

class LoanProductService:
    def __init__(self, db: Session):
        self.product_repo = LoanProductRepository(db)

    def create_product(
        self,
        name: str,
        interest_rate: float,
        max_amount: float
    ) -> LoanProduct:

        if interest_rate <= 0:
            raise ValueError("Interest rate must be positive")

        if max_amount <= 0:
            raise ValueError("Max amount must be positive")

        product = LoanProduct(
            name=name,
            interest_rate=interest_rate,
            max_amount=max_amount
        )
        return self.product_repo.create(product)

    def list_products(self):
        return self.product_repo.list()