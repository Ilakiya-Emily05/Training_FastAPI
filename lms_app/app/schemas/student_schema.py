from pydantic import BaseModel, EmailStr, Field

class StudentCreate(BaseModel):
    name: str = Field(..., min_length=2)
    email: EmailStr

class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True