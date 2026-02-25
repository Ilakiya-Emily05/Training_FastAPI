from sqlalchemy.orm import Session
from app.repositories.repayment_repository import RepaymentRepository
from app.repositories.application_repository import LoanApplicationRepository
from app.models.repayment import Repayment

class RepaymentService:
    def __init__(self, db: Session):
        self.repayment_repo = RepaymentRepository(db)
        self.application_repo = LoanApplicationRepository(db)

    def make_repayment(
        self,
        application_id: int,
        amount: float
    ) -> Repayment:

        application = self.application_repo.get_by_id(application_id)
        if not application:
            raise ValueError("Loan application not found")

        if application.status != "APPROVED":
            raise ValueError("Cannot repay unapproved loan")

        if amount <= 0:
            raise ValueError("Repayment amount must be positive")

        repayment = Repayment(
            loan_application_id=application_id,
            amount=amount
        )

        return self.repayment_repo.create(repayment)