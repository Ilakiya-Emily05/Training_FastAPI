from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.user_schema import UserCreate, UserRead
from app.services.user_service import UserService
from app.core.database import get_db

router = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    "/",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED
)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    try:
        return service.create_user(
            email=user.email,
            full_name=user.full_name
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get(
    "/{user_id}",
    response_model=UserRead
)
def get_user(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    try:
        return service.get_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))