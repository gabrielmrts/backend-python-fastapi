from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated, Optional
import jwt
from app.interfaces.token_interface import ITokenService
from app.schemas.token_schema import TokenData
from app.core.settings import Settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="sessions")


class TokenService(ITokenService):
    """Class for managing JWT tokens with enhanced validation"""

    def __init__(self: "TokenService") -> None:
        """Constructor"""
        self.secret_key = Settings().JWT_SECRET  # type: ignore
        self.algorithm = Settings().JWT_ALGORITHM  # type: ignore
        self.access_token_expire_minutes = Settings().JWT_EXPIRATION_MINUTES  # type: ignore # noqa

    def create_access_token(
        self: "TokenService",
        data: TokenData,
        expires_delta: Optional[timedelta] = None
    ) -> str:
        """
        Create Access Token with enhanced security

        Params:
            data: TokenData = data to encode
            expires_delta: Optional[timedelta] = Time to expire
        Returns:
            token: str
        Raises:
            ValueError: If invalid data is provided
        """
        if not data:
            raise ValueError("Token data cannot be empty")

        to_encode = data.model_dump().copy()
        time_now = datetime.now(timezone.utc)

        if expires_delta:
            expire = time_now + expires_delta
        else:
            expire = time_now + timedelta(minutes=self.access_token_expire_minutes)

        to_encode.update({
            "exp": expire,
            "iat": time_now,
            "nbf": time_now
        })

        try:
            encoded_jwt = jwt.encode(
                to_encode,
                self.secret_key,
                algorithm=self.algorithm
            )
            return encoded_jwt
        except Exception as err:
            raise ValueError(f"Failed to create token: {str(err)}") from err

    def get_token_data(
        self: "TokenService",
        token: str = Annotated[str, Depends(oauth2_scheme)]  # type: ignore # noqa
    ) -> TokenData:
        """
        Validate and extract token data with comprehensive error handling

        Params:
            token: str = JWT token to validate
        Returns:
            TokenData: Validated token data
        Raises:
            HTTPException: With appropriate status code and detail message
        """
        try:
            payload = jwt.decode(
                token,
                self.secret_key,
                algorithms=[self.algorithm],
                options={
                    "verify_signature": True,
                    "verify_exp": True,
                    "verify_iat": True,
                    "verify_nbf": True,
                    "require": ["exp", "iat", "nbf", "data"]
                }
            )

            token_data = payload.get("data")
            if not token_data:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid token data structure",
                    headers={"WWW-Authenticate": "Bearer"},
                ) from None

            return TokenData(**token_data)

        except jwt.ExpiredSignatureError as err:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired",
                headers={"WWW-Authenticate": "Bearer"},
            ) from err
        except jwt.InvalidTokenError as err:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
                headers={"WWW-Authenticate": "Bearer"},
            ) from err
        except Exception as err:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Failed to validate token: {str(err)}",
                headers={"WWW-Authenticate": "Bearer"},
            ) from err
