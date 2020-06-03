from api.models.api.user import UserAPI
from api.models.orm.user import UserORM
from api.services.crud import CRUDService


def test_create_user(db):

    user_api = UserAPI(username="user")
    created = CRUDService.create(db, user_api, UserORM)
    assert created.id
