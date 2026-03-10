import logging
from core.logger.logging_filters import RequestIdFilter

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(request_id)s | %(message)s",
)

logger = logging.getLogger()
logger.addFilter(RequestIdFilter())