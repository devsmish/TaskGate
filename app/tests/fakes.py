import uuid
from datetime import UTC, date, datetime


class FakeUser:
    def __init__(
        self,
        email: str,
        hashed_password: str,
        first_name: str | None = None,
        last_name: str | None = None,
        phone_number: str | None = None,
        date_of_birth: date | None = None,
    ) -> None:
        self.id = uuid.uuid4()
        self.email = email
        self.hashed_password = hashed_password
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.is_active = True
        self.is_employee = False
        self.created_at = datetime.now(UTC)

    @property
    def full_name(self) -> str:
        parts = [self.first_name, self.last_name]
        return " ".join(p for p in parts if p)


class FakeUserRepository:
    def __init__(self) -> None:
        self.users: dict[str, FakeUser] = {}

    async def get_by_email(self, email: str) -> FakeUser | None:
        return self.users.get(email)

    async def create(
        self,
        *,
        email: str,
        hashed_password: str,
        first_name: str | None = None,
        last_name: str | None = None,
        phone_number: str | None = None,
        date_of_birth: date | None = None,
    ) -> FakeUser:
        user = FakeUser(
            email=email,
            hashed_password=hashed_password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
        )
        self.users[email] = user
        return user
