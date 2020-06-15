from unittest.mock import patch

from api.core.errors import ServiceUnavailable


def test_service_unavailable(client):
    """ Tests ServiceUnavailable exception on /status endpoint. """

    with patch("api.routers.status.is_alive") as alive:
        alive.side_effect = [ServiceUnavailable()]
        response = client.get("/status")
        assert response.status_code == 503
        assert response.json()["detail"] == ServiceUnavailable.public_message
