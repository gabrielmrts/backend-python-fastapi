import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.dependencies import get_db, get_session_service
from app.schemas.session import SessionCreate
from app.services.session_service import SessionService
from sqlalchemy.orm import Session
from typing import Generator
from app.schemas.session import SessionResponse

client = TestClient(app)


class MockSessionService(SessionService):
    """A mock implementation of SessionService for testing purposes."""

    def create_session(
        self: "MockSessionService",
        session_data: SessionCreate,
        db: Session
    ) -> SessionResponse:
        """
        Creates a mocked session for testing.

        Args:
            session_data (SessionCreate): The session data.
            db (Session): The database session.

        Returns:
            dict[str, str]: A dictionary containing the mocked session token.
        """
        return SessionResponse(token="mocked_token")


@pytest.fixture
def override_get_session_service() -> Generator[MockSessionService, None, None]:
    """Provides a mocked session service for use in tests.

    Yields:
        MockSessionService: A mocked instance of the session service.
    """
    yield MockSessionService(token_service=None)  # type: ignore


@pytest.mark.parametrize(
    "override_get_session_service",
    [MockSessionService(token_service=None)],  # type: ignore
    indirect=True
)
def test_create_session_success(
    override_get_session_service: MockSessionService,
    test_db_session: Session,
    monkeypatch: pytest.MonkeyPatch
) -> None:
    """Tests the successful creation of a session.

    Args:
        override_get_session_service (MockSessionService): The mocked session service.
        test_db_session (Session): The test database session.
        monkeypatch (pytest.MonkeyPatch): The object used to override dependencies.
    """
    monkeypatch.setattr(
        app,
        'dependency_overrides',
        {
            get_session_service: lambda: override_get_session_service,
            get_db: lambda: test_db_session
        }
    )

    session_data: dict[str, str] = {
        "cpf": "90549126260",
        "password": "password123"
    }

    response = client.post("/public/sessions", json=session_data)

    assert response.status_code == 200
    assert response.json() == {"token": "mocked_token"}
