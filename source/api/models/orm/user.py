from sqlalchemy import Column
from sqlalchemy import String

from api.models.orm.base import BaseORM


class UserORM(BaseORM):

    __tablename__ = "users"

    username = Column(String, nullable=False)
