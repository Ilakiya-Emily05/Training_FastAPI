from pydantic import BaseModel
# what client sends
class ProductCreate(BaseModel):
    name: str
    interest_rate: float
    max_amount: float


# what API returns
class ProductRead(BaseModel):
    id: int
    name: str
    interest_rate: float
    max_amount: float

    class Config:
        from_attributes = True  # SQLAlchemy -> Pydantic