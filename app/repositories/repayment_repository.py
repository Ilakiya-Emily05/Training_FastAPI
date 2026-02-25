from sqlalchemy.orm import Session
from app.models.repayment import Repayment

class RepaymentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, repayment: Repayment) -> Repayment:
        self.db.add(repayment)
        self.db.commit()
        self.db.refresh(repayment)
        return repayment

    def list_by_application(self, application_id: int) -> list[Repayment]:
        return self.db.query(Repayment).filter(
            Repayment.loan_application_id == application_id
        ).all()