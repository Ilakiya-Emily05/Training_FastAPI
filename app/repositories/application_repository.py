from sqlalchemy.orm import Session
from app.models.loan_application import LoanApplication

class LoanApplicationRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, application_id: int) -> LoanApplication | None:
        return self.db.query(LoanApplication).filter(
            LoanApplication.id == application_id
        ).first()

    def create(self, application: LoanApplication) -> LoanApplication:
        self.db.add(application)
        self.db.commit()
        self.db.refresh(application)
        return application

    def list_by_user(self, user_id: int) -> list[LoanApplication]:
        return self.db.query(LoanApplication).filter(
            LoanApplication.user_id == user_id
        ).all()