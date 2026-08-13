from httpx import ASGITransport, AsyncClient

from app.api.v1.auth import get_auth_service
from app.main import app
from app.services.auth_service import AuthService
from app.tests.fakes import FakeUserRepository


async def test_register_endpoint_success() -> None:
    app.dependency_overrides[get_auth_service] = lambda: AuthService(FakeUserRepository())
    try:
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as client:
            response = await client.post(
                "/api/v1/auth/register",
                json={
                    "email": "bob@example.com",
                    "password": "supersecret",
                    "first_name": "Bob",
                    "last_name": "Jones",
                },
            )
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 201
    body = response.json()
    assert body["email"] == "bob@example.com"
    assert "password" not in body
    assert "hashed_password" not in body


async def test_register_endpoint_duplicate_email_returns_409() -> None:
    shared_repository = FakeUserRepository()
    app.dependency_overrides[get_auth_service] = lambda: AuthService(shared_repository)
    try:
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as client:
            payload = {
                "email": "carol@example.com",
                "password": "supersecret",
                "full_name": "Carol",
            }
            first = await client.post("/api/v1/auth/register", json=payload)
            second = await client.post("/api/v1/auth/register", json=payload)
    finally:
        app.dependency_overrides.clear()

    assert first.status_code == 201
    assert second.status_code == 409
