from datetime import datetime

from dateutil.tz import gettz

from api.core.config import settings


def now() -> datetime:
    """ Returns current datetime with timezone. """

    tz = gettz(settings.TIMEZONE)
    current_datetime = datetime.now(tz)
    return current_datetime
