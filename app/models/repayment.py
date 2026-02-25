from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Repayment(Base):
    __tablename__ = "repayments"

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)

    loan_application_id = Column(
        Integer,
        ForeignKey("loan_applications.id"),
        nullable=False
    )

    loan_application = relationship("LoanApplication")