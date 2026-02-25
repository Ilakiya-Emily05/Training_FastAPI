from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LoanApplicationBase(BaseModel):
    amount: float
    tenure_months: int

class LoanApplicationCreate(LoanApplicationBase):
    user_id: int
    product_id: int

class LoanApplicationRead(LoanApplicationBase):
    id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True