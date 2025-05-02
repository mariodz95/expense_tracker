import json
import logging
from datetime import datetime, timezone


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": datetime.now(timezone.utc).replace(tzinfo=None),
            "level": record.levelname,
            "message": record.getMessage(),
            "file": f"{record.pathname}:{record.lineno}",
        }

        if record.exc_info:
            log_record["exception"] = self.formatException(record.exc_info)

        return json.dumps(log_record)


def setup_logger(name: str = "fastapi-logger") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.ERROR)

    if logger.hasHandlers():
        logger.handlers.clear()

    handler = logging.StreamHandler()
    handler.setFormatter(JsonFormatter())
    logger.addHandler(handler)
    return logger
