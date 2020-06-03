from functools import lru_cache
from os import getenv

from pydantic import BaseSettings


class BaseConfig(BaseSettings):

    dsn: str = getenv("DB_DSN")


@lru_cache()
def get_api_settings() -> BaseConfig:
    return BaseConfig()


settings = get_api_settings()
