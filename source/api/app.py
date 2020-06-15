from fastapi import FastAPI

from api.core.config import settings
from api.routers.status import router as status
from api.routers.users import router as users


def start_app():
    """ Returns running app. """
    app = FastAPI(debug=settings.DEBUG, title=settings.APP_NAME)
    app.include_router(users, prefix="/users")
    app.include_router(status, prefix="/status")
    return app


app = start_app()
