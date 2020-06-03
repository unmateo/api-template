from pytest import raises

from api.models.orm.user import UserORM


def test_user():
    assert UserORM(username="user")
