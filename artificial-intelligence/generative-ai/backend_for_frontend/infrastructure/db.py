from functools import lru_cache
from typing import Iterator

from infrastructure.repositories.settings import settings
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker


# REF-009-DB-CONNECTION-CONFIG, REF-009-DB-SESSION-MANAGEMENT, REF-009-DB-SESSION-CACHING
# REF-009-CACHING-MEMOIZATION
@lru_cache()
def get_engine() -> Engine:
    """
    Engine creation

    :return: Engine: A SQLAlchemy engine instance.
    """
    return create_engine(settings.database_url)


# REF-006-FACTORY-DESIGN-PATTERN
@lru_cache()
def get_session_factory() -> sessionmaker:
    """
    Session maker

    :return: sessionmaker: A SQLAlchemy session factory.
    """
    return sessionmaker(autocommit=False, autoflush=False, bind=get_engine())


def get_db() -> Iterator[Session]:
    """
    Session Management

    :return: Session: A SQLAlchemy session object.
    """
    db_session = get_session_factory()()

    # REF-009-CONTEXT-MANAGER, REF-006-DEPENDENCY-INJECTION-DESIGN-PATTERN
    try:
        yield db_session
    finally:
        db_session.close()
