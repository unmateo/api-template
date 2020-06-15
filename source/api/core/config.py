from functools import lru_cache

from pydantic import BaseSettings


class BaseConfig(BaseSettings):

    APP_NAME: str = "app"
    DB_DSN: str
    DEBUG: bool = False
    LOG_LEVEL: str
    TIMEZONE: str = "UTC"


@lru_cache()
def get_api_settings() -> BaseConfig:
    return BaseConfig()


settings = get_api_settings()
