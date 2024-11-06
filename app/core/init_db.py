from app.core.database import Base, engine


def init_database() -> None:
    """
    Initializes the database.

    This function sets up the initial state of the database.
    """
    Base.metadata.create_all(bind=engine)
