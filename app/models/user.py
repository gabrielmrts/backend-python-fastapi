from sqlalchemy import (
    Integer,
    String,
    Numeric
)
from app.core.database import Base
from passlib.context import CryptContext
from sqlalchemy.orm import mapped_column, Mapped

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(Base):  # type: ignore
    """
    Represents a user in the system with personal and financial details.

    Attributes:
        id (Column): The primary key of the user, an integer that is auto-incremented.
        account_number (Column): The account number of the user, stored as an integer
            and must be unique.
        name (Column): The name of the user, stored as a non-nullable string.
        cpf (Column): The CPF (Cadastro de Pessoas Físicas) of the user, stored as a
            unique and non-nullable string.
        password (Column): The hashed password of the user, stored as a non-nullable
            string.
        balance (Column): The account balance of the user, stored as a numeric value
            with a precision of 17 digits and 2 decimal places. Defaults to 0.
    """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)  # noqa
    account_number: Mapped[int] = mapped_column(Integer, unique=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    balance: Mapped[float] = mapped_column(Numeric(17, 2), default=0)

    def __init__(self: "User", cpf: str, password: str) -> None:
        """Init the user"""
        self.cpf = cpf
        self.password = self.hash_password(password)

    def hash_password(self: "User", password: str) -> str:
        """Hash a password for storage."""
        return pwd_context.hash(password)  # type: ignore

    def verify_password(self: "User", password: str) -> bool:
        """Verify if the provided password matches the stored hash."""
        return pwd_context.verify(password, self.password)  # type: ignore
