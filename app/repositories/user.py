from app.models.user import User
from app.repositories.base import BaseRepository
from sqlalchemy.orm import Session


class UserRepository(BaseRepository):  # type: ignore
    """
    A repository for managing database operations specific to the `User` model.

    Inherits from `BaseRepository` and provides a concrete implementation for
        user-specific database interactions.
    """

    def __init__(self: "UserRepository") -> None:
        """
        Initializes the `UserRepository` with the `User` model.

        This constructor calls the `BaseRepository` initializer and passes the `User`
        model, allowing the repository to perform CRUD operations for user data.
        """
        super().__init__(User)

    def get_by_cpf(self: "UserRepository", db: Session, cpf: str) -> User | None:
        """Get user by cpf"""
        return db.query(User).filter(User.cpf == cpf).first()
