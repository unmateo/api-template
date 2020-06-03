from uuid import uuid4

from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def generate_id() -> str:
    return str(uuid4())


class BaseORM(Base):

    __abstract__ = True

    id = Column(
        String(), primary_key=True, default=generate_id, unique=True, nullable=False,
    )
    deleted = Column(Boolean, default=False)
