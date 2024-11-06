import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.database import Base
from typing import Generator, Any


@pytest.fixture(scope="module")
def test_db_session() -> Generator[Any, Any, Any]:
    """Creates an in-memory SQLite database session for testing.

    This fixture sets up an in-memory SQLite database, initializes the
    tables using SQLAlchemy, and yields a database session for use in tests.
    After the test is complete, it closes the session and drops all tables.

    Yields:
        Generator[Any, Any, Any]: A SQLAlchemy database session.
    """
    engine = create_engine("sqlite:///:memory:")
    testing_session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base.metadata.create_all(bind=engine)

    db = testing_session_local()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)
