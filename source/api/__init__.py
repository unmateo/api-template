from fastapi import FastAPI

from api.config import settings
from api.models.orm.base import BaseORM
from api.routers.users import router as users
from api.services.database import get_engine

app = FastAPI()

app.include_router(users, prefix="/users")


@app.on_event("startup")
def create_metadata():
    """ This should probably be somewhere else """
    engine = get_engine(settings.dsn)
    BaseORM.metadata.create_all(bind=engine)
