from pydantic import BaseModel


class TokenData(BaseModel):
    """
    Schema for representing token payload data.

    This model is used to structure the data embedded within an authentication token,
    typically for identifying the authenticated user.

    Attributes:
        sub (str): The user ID.
    """

    sub: str
