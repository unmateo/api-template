from unittest.mock import Mock
from unittest.mock import patch

from pytest import raises

from api.core.database import get_engine
from api.core.database import get_maker
from api.core.database import get_session
from api.core.database import is_alive


def test_engine(dsn):
    engine = get_engine(dsn)
    assert engine


def test_maker(dsn):
    maker = get_maker(dsn)
    assert maker


def test_session(dsn):
    with get_session(dsn) as session:
        assert session


def test_session_rollback_on_exception():
    with patch("api.core.database.get_maker") as maker:
        session = Mock()
        session.execute.side_effect = [Exception()]
        maker.return_value.return_value = session
        with raises(Exception), get_session("fake_dsn"):
            session.execute("fake_query")
        session.rollback.assert_called_once()
        session.close.assert_called_once()


def test_session_is_closed():
    with patch("api.core.database.get_maker") as maker:
        session = Mock()
        maker.return_value.return_value = session
        with get_session("fake_dsn"):
            session.execute("fake_query")
        session.close.assert_called_once()


def test_is_alive(dsn):
    with get_session(dsn) as session:
        assert is_alive(session)
