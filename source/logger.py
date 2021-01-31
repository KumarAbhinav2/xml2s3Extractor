from source import settings
import logging
import logging.handlers
logging.basicConfig(
    format='%(asctime)s\t%(name)-16s\t%(funcName)22s:%(lineno)d\t%(levelname)s\t%(message)s',
    level=logging.INFO)

LOG_HOST = getattr(settings, 'LOG_HOST', None)
LOG_URI = getattr(settings, 'LOG_URI', None)


def getLogger(name):
    log = logging.getLogger(name)
    if LOG_HOST is not None and LOG_URI is not None:
        http_handler = logging.handlers.HTTPHandler(
            LOG_HOST,
            LOG_URI,
            method='POST',
        )
        log.addHandler(http_handler)
    return log