from fastapi.routing import APIRouter
from app.schemas.session import SessionCreate, SessionResponse
from fastapi import Depends
from app.dependencies import get_session_service, get_db
from sqlalchemy.orm import Session
from app.services.session_service import SessionService


router = APIRouter(prefix="/public")


@router.post("/sessions", tags=["Sessions"], response_model=SessionResponse)
def create_session(
    body: SessionCreate,
    session_service: SessionService = Depends(get_session_service),  # noqa
    db: Session = Depends(get_db)  # noqa
) -> SessionResponse:
    """
    Creates a new session.

    Args:
        body (SessionCreate): The body of the request containing session details.
        session_service (SessionService, optional): The session service dependency for
            handling session operations.
        db (Session, optional): The database session dependency. Defaults to an
            instance provided by `get_db`.

    Returns:
        SessionResponse: The created session response containing session information.
    """
    return session_service.create_session(body, db)
