from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from sqlalchemy.orm import Session

from api.core.database import is_alive
from api.core.dependencies import db
from api.core.errors import ServiceUnavailable


router = APIRouter()


@router.get("/", status_code=status.HTTP_204_NO_CONTENT)
def get_status(db: Session = Depends(db)):
    if not is_alive(db):
        raise ServiceUnavailable("Database down")
