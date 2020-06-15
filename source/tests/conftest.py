from pytest import fixture
from starlette.testclient import TestClient

from api.app import app
from api.core.config import settings
from api.core.database import get_engine
from api.core.database import get_session
from api.models.orm.base import BaseORM


@fixture(scope="session")
def dsn():
    return "sqlite://///app/source/tests/template-api.db?check_same_thread=False"


@fixture()
def renew_db(dsn):
    engine = get_engine(dsn)
    BaseORM.metadata.drop_all(engine)
    BaseORM.metadata.create_all(engine)


@fixture()
def db(dsn):
    with get_session(dsn) as session:
        yield session


@fixture()
def clean_db(renew_db, db):
    yield db


@fixture()
def client(dsn, renew_db):
    settings.DB_DSN = dsn
    client = TestClient(app)
    return client
