import pytest

from app.services.auth_service import AuthService, EmailAlreadyRegisteredError
from app.tests.fakes import FakeUserRepository


async def test_register_user_success() -> None:
    service = AuthService(FakeUserRepository())

    user = await service.register_user(
        email="alice@example.com", password="supersecret", first_name="Alice", last_name="Smith"
    )

    assert user.email == "alice@example.com"
    assert user.full_name == "Alice"
    assert user.hashed_password != "supersecret"


async def test_register_user_duplicate_email_raises() -> None:
    repository = FakeUserRepository()
    service = AuthService(repository)
    await service.register_user(
        email="alice@example.com", password="supersecret", first_name="Alice", last_name="Smith"
    )

    with pytest.raises(EmailAlreadyRegisteredError):
        await service.register_user(
            email="alice@example.com", password="another-pass", first_name="Al", last_name="Sm"
        )
