from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class LoanApplication(Base):
    __tablename__ = "loan_applications"

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    status = Column(String, default="PENDING")

    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("loan_products.id"))

    user = relationship("User", back_populates="loan_applications")
    product = relationship("LoanProduct", back_populates="loan_applications")