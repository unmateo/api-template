from pydantic import BaseModel


class BaseAPI(BaseModel):
    class Config:
        orm_mode = True
