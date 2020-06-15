from unittest.mock import patch


def test_status_ok(client):
    """ Tests /status endpoint on success"""
    endpoint = f"/status"
    response = client.get(endpoint)
    assert response.status_code == 204


def test_status_not_ok(client):
    """ Tests /status endpoint on failure"""
    endpoint = f"/status"
    with patch("api.routers.status.is_alive") as alive:
        alive.return_value = False
        response = client.get(endpoint)
        assert response.status_code == 503
