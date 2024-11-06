from abc import ABC, abstractmethod
from app.schemas.token_schema import TokenData
from typing import Optional
from datetime import timedelta


class ITokenEncoder(ABC):
    """An interface for encoding and decoding tokens."""

    @abstractmethod
    def encode(
        self: "ITokenEncoder",
        data: TokenData,
        secret: str,
        algorithm: str
    ) -> str:
        """Encodes data into a token.

        Args:
            data (TokenData): The data to be encoded into the token.
            secret (str): The secret key used for encoding.
            algorithm (str): The algorithm used for encoding.

        Returns:
            str: The encoded token.
        """
        pass

    @abstractmethod
    def decode(
        self: "ITokenEncoder",
        token: str,
        secret: str,
        algorithms: list[str]
    ) -> TokenData:
        """Decodes a token into data.

        Args:
            token (str): The token to be decoded.
            secret (str): The secret key used for decoding.
            algorithms (list[str]): The list of algorithms allowed for decoding.

        Returns:
            TokenData: The decoded data.
        """
        pass


class ITokenService(ABC):
    """An interface for a token service handling token creation and validation."""

    @abstractmethod
    def create_access_token(
        self: "ITokenService",
        data: TokenData,
        expires_delta: Optional[timedelta] = None
    ) -> str:
        """
        Creates an access token with embedded data and optional expiration.

        This method encodes the provided data into a JWT, adding claims for
        expiration (`exp`), issued at (`iat`), and not before (`nbf`). If no
        expiration delta is provided, a default value is used.

        Args:
            data (TokenData): The data to embed in the JWT payload.
            expires_delta (Optional[timedelta]): An optional time delta for the
                token's expiration. If None, a default expiration period is used.

        Returns:
            str: The generated JWT token as a string.

        Raises:
            ValueError: If the provided data is invalid or token creation fails.
        """
        pass

    @abstractmethod
    def get_token_data(
        self: "ITokenService",
        token: str
    ) -> TokenData:
        """
        Validates and extracts data from a given JWT token.

        This method is responsible for decoding the token, verifying its signature,
        and ensuring that required claims (e.g., 'exp', 'iat', 'nbf') are present
        and valid. If the token is invalid or any checks fail, an appropriate
        exception is raised.

        Args:
            token (str): The JWT token to be validated and decoded.

        Returns:
            TokenData: The extracted data as a `TokenData` object.

        Raises:
            HTTPException: Raised with status code 401 if the token is expired,
            has an invalid structure, or fails validation checks.
        """
        pass
