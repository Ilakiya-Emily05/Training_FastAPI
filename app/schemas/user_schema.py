from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    full_name: str

class UserCreate(UserBase):
    pass  # password can be added later if needed

class UserRead(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True