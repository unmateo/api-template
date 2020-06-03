from api.models.api.user import UserAPI


def test_create(client):
    user = UserAPI(username="user")
    response = client.post("/users/", json=user.dict())
    assert response.status_code == 200
