from fastapi import HTTPException, Request, Response, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from typing import Callable, Awaitable
import re
from app.services.token_service import TokenService


class AuthenticationMiddleware(BaseHTTPMiddleware):
    """
    Authentication Middleware.

    This middleware is responsible for handling authentication-related logic in the
    application.
    It checks the authorization header in the request and verifies the token to ensure
    the user is authenticated.
    If the token is valid, the request is forwarded to the next middleware in the stack.
    If the token is invalid or missing, a 401 Unauthorized response is returned.

    Attributes:
        token_service (TokenService): An instance of the TokenService class, used
        to verify the token.
    """

    def __init__(
        self: "AuthenticationMiddleware",
        app: Callable[[Request], Awaitable[Response]]
    ) -> None:
        """
        Initialize the AuthenticationMiddleware.

        Args:
            app (Callable[[Request], Awaitable[Response]]): The ASGI application to be
            wrapped by the middleware.
        """
        self.token_service = TokenService()

    async def dispatch(
        self: "AuthenticationMiddleware",
        request: Request,
        call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        """
        Dispatch the request through the middleware.

        This method is called for each incoming request. It checks the request path and
            method to determine if authentication is required.
        If authentication is required, it retrieves the token from the Authorization
            header and verifies it using the TokenService.
        If the token is valid, the request is forwarded to the next middleware
            in the stack.
        If the token is invalid or missing, a 401 Unauthorized response is returned.

        Args:
            request (Request): The incoming request object.
            call_next (Callable[[Request], Awaitable[Response]]): The next middleware
            or endpoint to be called.

        Returns:
            Response: The response object to be returned to the client.
        """
        if re.match("/+public/*", request.url.path) or request.method == "OPTIONS":
            return await call_next(request)

        token = request.headers.get("Authorization")

        if not token:
            return JSONResponse({"msg": "invalid token"}, status.HTTP_401_UNAUTHORIZED)

        try:
            token = token.replace('Bearer ', '')
            self.token_service.get_token_data(token)
            return await call_next(request)
        except HTTPException:
            return JSONResponse({"msg": "invalid token"}, status.HTTP_401_UNAUTHORIZED)
