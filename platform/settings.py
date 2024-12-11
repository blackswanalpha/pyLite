# Settings for desktop platform
import logging

logging.basicConfig(filename='development.log', level=logging.INFO)
logger = logging.getLogger(__name__)

def log_message(message):
    logger.info(message)
