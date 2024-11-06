from typing import Generic, TypeVar, Type
from sqlalchemy.orm import Session
from app.core.database import Base

ModelType = TypeVar("ModelType", bound=Base)  # type: ignore


class BaseRepository(Generic[ModelType]):
    """
    A base repository class for performing common database operations.

    Attributes:
        model (Type[ModelType]): The database model associated with the repository.
    """

    def __init__(
        self: "BaseRepository",  # type: ignore
        model: Type[ModelType]
    ) -> None:
        """
        Initializes the repository with a specific model.

        Args:
            model (Type[ModelType]): The database model that this repository will
                handle.
        """
        self.model = model

    def get(
        self: "BaseRepository",  # type: ignore
        db: Session,
        id_: int
    ) -> ModelType | None:
        """
        Retrieves a single record by its ID.

        Args:
            db (Session): The database session used to query the data.
            id_ (int): The ID of the record to retrieve.

        Returns:
            ModelType | None: The record if found, otherwise None.
        """
        return db.query(self.model).filter(self.model.id == id_).first()
