from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from api.core.dependencies import db
from api.models.api.user import UserAPI
from api.models.orm.user import UserORM
from api.services.crud import CRUDService


router = APIRouter()


@router.post("/")
def create_user(user_api: UserAPI, db: Session = Depends(db)):
    user = CRUDService.create(db, user_api, UserORM)
    return user
