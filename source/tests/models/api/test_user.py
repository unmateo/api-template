from pytest import raises

from api.models.api.user import UserAPI


def test_user():
    assert UserAPI(username="user")


def test_username_required():
    with raises(ValueError):
        UserAPI()
