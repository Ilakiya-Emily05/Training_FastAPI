from pydantic import BaseModel
from datetime import datetime

class RepaymentBase(BaseModel):
    amount: float
    due_date: datetime

class RepaymentCreate(RepaymentBase):
    loan_application_id: int

class RepaymentRead(RepaymentBase):
    id: int
    is_paid: bool

    class Config:
        from_attributes = True