import uuid

from sqlalchemy import CHAR, TIMESTAMP, Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql import func


# REF-009-DATA-MODELLING
class Base(DeclarativeBase):
    pass


def generate_ordered_uuid() -> uuid.UUID:
    """
    UUID generation implemented as the function so SQLAlchemy calls it every time a new row is created.

    :return: uuid.UUID
    """
    return uuid.uuid1()


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=generate_ordered_uuid)
    email = Column(String(255), unique=True, nullable=False, index=True)
    username = Column(String(150), unique=True, nullable=False, index=True)
    password = Column(CHAR(60), nullable=False)

    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())
