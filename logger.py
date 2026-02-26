import logging
from logging.handlers import RotatingFileHandler


# ==========================================
# Logging Setup
# ==========================================

SHORT_LOG_FORMAT = "[%(asctime)s - %(levelname)s] - %(name)s - %(message)s"
FULL_LOG_FORMAT = "%(asctime)s - [%(levelname)s] - %(name)s - %(message)s (%(filename)s:%(lineno)d)"


# Configure logging system
logging.basicConfig(
    level=logging.INFO,
    format=SHORT_LOG_FORMAT,
    handlers=[
        RotatingFileHandler("logs.txt", maxBytes=5 * 1024 * 1024, backupCount=10),

        logging.StreamHandler()
    ]
)

logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
