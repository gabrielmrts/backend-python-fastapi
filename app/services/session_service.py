from app.schemas.session import SessionCreate, SessionResponse
from app.interfaces.token_interface import ITokenService
from app.schemas.token_schema import TokenData
from app.repositories.user import UserRepository
from sqlalchemy.orm import Session
from fastapi import HTTPException


class SessionService:
    """
    Service for handling session-related operations.

    This service provides methods for creating and managing user sessions,
    including token generation for authenticated users.

    Attributes:
        token_service (ITokenService): The token service used for creating and
            validating access tokens.
        repository (UserRepository): The repository used for querying user data.
    """

    def __init__(
        self: "SessionService",
        token_service: ITokenService
    ) -> None:
        """
        Initializes the `SessionService` with the required dependencies.

        Args:
            token_service (ITokenService): An implementation of `ITokenService` used
                for token operations.
        """
        self.token_service: ITokenService = token_service
        self.repository = UserRepository()

    def create_session(
        self: "SessionService",
        session_data: SessionCreate,
        db: Session
    ) -> SessionResponse:
        """
        Creates a user session and generates an access token.

        This method takes user credentials, verifies them, and creates a session
        by generating an authentication token.

        Args:
            session_data (SessionCreate): The input data containing user credentials.
            db (Session): The database session used for user verification and
                data retrieval.

        Returns:
            SessionResponse: A response object containing the generated access token.

        Raises:
            ValueError: If the user credentials are invalid or user verification fails.
        """
        user = self.repository.get_by_cpf(next(db), session_data.cpf)  # type: ignore
        if not user or not user.verify_password(session_data.password):
            raise HTTPException(401, "Incorrect credentials")

        token_data = TokenData(sub=str(user.id))
        token = self.token_service.create_access_token(token_data)

        return SessionResponse(token=token)
