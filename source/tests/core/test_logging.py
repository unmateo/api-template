from logging import WARNING

from api.core.logging import logger


def test_logger(caplog):
    message = "test message"
    logger.warning(message)
    assert len(caplog.records) == 1
    logger_, level_, message_ = caplog.record_tuples[0]
    assert level_ == WARNING
    assert message_ == message
