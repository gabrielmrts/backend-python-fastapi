from pydantic import BaseModel, field_validator
from app.validators.cpf import CPFValidator
from typing import Type


class SessionCreate(BaseModel):
    """
    Schema for creating a session.

    This model is used for validating the input data required to create a user session,
    such as authentication credentials.

    Attributes:
        cpf (str): The CPF (Cadastro de Pessoas Físicas) of the user, which must
            be valid.
        password (str): The password of the user for authentication.
    """

    cpf: str
    password: str

    @field_validator('cpf')
    @classmethod
    def cpf_must_be_valid(cls: Type['SessionCreate'], value: str) -> str:
        """
        Validates the CPF field to ensure it is in a valid format.

        Args:
            value (str): The CPF provided by the user.

        Returns:
            str: The validated CPF.

        Raises:
            ValueError: If the CPF is not valid.
        """
        if not CPFValidator.is_valid(value):
            raise ValueError("Invalid CPF")
        return value


class SessionResponse(BaseModel):
    """
    Schema for returning session data.

    This model is used to format the response data for a created session,
    typically after successful authentication.

    Attributes:
        token (str): The authentication token generated for the session.
    """

    token: str
