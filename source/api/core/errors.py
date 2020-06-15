from fastapi import HTTPException

from api.core.logging import logger


class HandledException(HTTPException):

    public_message = "Ups! There was an error."
    status_code = 500

    def __init__(self, private_message=""):
        super().__init__(status_code=self.status_code, detail=self.public_message)
        logger.warning(f"{self}: {private_message}")

    def __str__(self):
        return self.__class__.__name__


class ServiceUnavailable(HandledException):

    public_message = "Service unavailable. Try again later."
    status_code = 503
