import os
from pydantic_settings import BaseSettings

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://dev:dev@localhost:55432/dev"
)


class Settings(BaseSettings):
    """A class for application settings.

    This class holds configuration settings for the application, including
        JWT and database configurations.
    The settings are loaded from environment variables or an `.env` file.
    """

    JWT_SECRET: str
    """str: The secret key used for JWT encoding and decoding."""

    JWT_ALGORITHM: str
    """str: The algorithm used for JWT token creation."""

    JWT_EXPIRATION_MINUTES: int
    """int: The duration in minutes before a JWT token expires."""

    DATABASE_URL: str
    """str: The database connection URL."""

    CORS_ALLOWED_ORIGINS: str
    """str: Allowed CORS Origins"""

    PROJECT_TITLE: str
    """str: Title of the project"""

    PROJECT_DESCRIPTION: str
    """str: Description of the project"""

    PROJECT_VERSION: str
    """str: Current version of the project"""

    class Config:
        """Configuration for the Settings class.

        This inner class specifies configuration options such as
            loading variables from a `.env` file.
        """

        env_file = ".env"
        """str: Specifies the path to the environment file."""
