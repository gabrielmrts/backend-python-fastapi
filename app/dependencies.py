from fastapi import Depends
from functools import lru_cache
from app.services.token_service import TokenService
from app.services.session_service import SessionService
from app.core.settings import Settings
from typing import Generator, Any
from app.core.database import get_database


@lru_cache()
def get_settings() -> Settings:
    """
    Retrieves the application settings with caching.

    This function uses an LRU (Least Recently Used) cache to optimize performance
    by storing the settings instance, ensuring it is only initialized once.

    Returns:
        Settings: An instance of the application settings.
    """
    return Settings()  # type: ignore


def get_token_service(
    settings: Settings = Depends(get_settings)  # noqa
) -> TokenService:
    """
    Provides an instance of TokenService.

    This function creates and returns an instance of `TokenService` with the
    necessary dependencies injected.

    Args:
        settings (Settings): The application settings, injected via dependency.

    Returns:
        TokenService: An instance of the `TokenService` class.
    """
    return TokenService()


def get_db() -> Generator[Any, Any, Any]:
    """
    Provides a database session generator.

    This function yields a database session and ensures it is properly closed
    after use.

    Yields:
        Generator[Any, Any, Any]: A generator for database sessions.
    """
    return get_database()


def get_session_service(
    token_service: TokenService = Depends(get_token_service)  # noqa
) -> SessionService:
    """
    Provides an instance of SessionService.

    This function creates and returns an instance of `SessionService` with the
    required `TokenService` dependency injected.

    Args:
        token_service (TokenService): The token service, injected via dependency.

    Returns:
        SessionService: An instance of the `SessionService` class.
    """
    return SessionService(token_service)
