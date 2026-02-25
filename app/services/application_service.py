from sqlalchemy.orm import Session
from app.repositories.application_repository import LoanApplicationRepository
from app.repositories.user_repository import UserRepository
from app.repositories.product_repository import LoanProductRepository
from app.models.loan_application import LoanApplication

class LoanApplicationService:
    def __init__(self, db: Session):
        self.application_repo = LoanApplicationRepository(db)
        self.user_repo = UserRepository(db)
        self.product_repo = LoanProductRepository(db)

    def apply_for_loan(
        self,
        user_id: int,
        product_id: int,
        amount: float
    ) -> LoanApplication:

        user = self.user_repo.get_by_id(user_id)
        if not user or not user.is_active:
            raise ValueError("Invalid or inactive user")

        product = self.product_repo.get_by_id(product_id)
        if not product:
            raise ValueError("Loan product not found")

        if amount > product.max_amount:
            raise ValueError("Requested amount exceeds product limit")

        application = LoanApplication(
            user_id=user_id,
            product_id=product_id,
            amount=amount,
            status="PENDING"
        )

        return self.application_repo.create(application)