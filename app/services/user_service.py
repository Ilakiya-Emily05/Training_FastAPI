from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.models.user import User

class UserService:
    def __init__(self, db: Session):
        self.user_repo = UserRepository(db)

    def create_user(self, email: str, full_name: str) -> User:
        existing = self.user_repo.get_by_email(email)
        if existing:
            raise ValueError("User with this email already exists")

        user = User(
            email=email,
            full_name=full_name,
            is_active=True
        )
        return self.user_repo.create(user)

    def get_user(self, user_id: int) -> User:
        user = self.user_repo.get_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        return user