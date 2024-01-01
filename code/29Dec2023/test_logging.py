import logging


def test_print_logs():
    LOGGER = logging.getLogger(__name__)
    LOGGER.info("This is information log")
    LOGGER.warning("This is warning log")
    LOGGER.error("This is error log")
    LOGGER.critical("This is critical log")
