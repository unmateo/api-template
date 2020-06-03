from pytest import fixture
from starlette.testclient import TestClient

from api import app
from api.config import settings
from api.models.orm.base import BaseORM
from api.services.database import get_engine
from api.services.database import get_session


@fixture(scope="session")
def dsn():
    return "sqlite://///app/source/tests/api_test.db?check_same_thread=False"


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
    settings.dsn = dsn
    client = TestClient(app)
    return client
