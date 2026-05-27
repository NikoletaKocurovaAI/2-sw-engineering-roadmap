from typing import Optional

from infrastructure.models import User
from sqlalchemy.orm import Session


# REF-011-API-CRUD-OPERATIONS, REF-009-DB-ORM
def get_user_by_username(db: Session, username: str) -> Optional[User]:
    return db.query(User).filter(User.username == username).first()
