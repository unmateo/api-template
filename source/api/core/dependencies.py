from api.core.config import settings
from api.core.database import get_session


def db():
    with get_session(settings.DB_DSN) as session:
        yield session
