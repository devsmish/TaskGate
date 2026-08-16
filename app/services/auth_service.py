from datetime import date

from app.core.security import hash_password
from app.models.user import User
from app.repositories.user_repository import UserRepository


class EmailAlreadyRegisteredError(Exception):
    """Raised when the email is already taken by another user."""


class AuthService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    async def register_user(
        self,
        *,
        email: str,
        password: str,
        first_name: str | None = None,
        last_name: str | None = None,
        phone_number: str | None = None,
        date_of_birth: date | None = None,
    ) -> User:
        existing_user = await self.repository.get_by_email(email)
        if existing_user is not None:
            raise EmailAlreadyRegisteredError(email)

        return await self.repository.create(
            email=email,
            hashed_password=hash_password(password),
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
        )
