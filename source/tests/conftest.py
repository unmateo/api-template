from pytest import fixture
from starlette.testclient import TestClient

from api import app


@fixture
def client():
    client = TestClient(app)
    return client
