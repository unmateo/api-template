from uuid import uuid4

from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy.ext.declarative import declarative_base

from api.core.date import now
from api.models.orm.guid import GUID


Base = declarative_base()


class BaseORM(Base):

    __abstract__ = True

    id = Column(GUID, primary_key=True, default=uuid4, unique=True)
    created_at = Column(DateTime, default=now, nullable=False)
    updated_at = Column(DateTime, default=now, nullable=False, onupdate=now)
    deleted = Column(Boolean, default=False, nullable=False)

    def __repr__(self):
        return f"{self.__class__.__name__}<{self.id}>"
