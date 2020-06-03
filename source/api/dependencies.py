from api.config import settings
from api.services.database import get_session


def db():
    with get_session(settings.dsn) as session:
        yield session
