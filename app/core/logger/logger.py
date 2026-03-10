# core/logger.py
import logging
from core.middleware.request_context import request_id_ctx
from core.middleware.request_context import request_id_ctx

logger = logging.getLogger("app")


class RequestIdFilter(logging.Filter):
    def filter(self, record):
        record.request_id = request_id_ctx.get() or "-"
        return True
    
def info(message: str, **kwargs):
    logger.info(
        message,
        extra={
            "request_id": request_id_ctx.get(),
            **kwargs
        }
    )
def error(message:str, exc_info:bool = True, **kwargs):
    logger.error(
        message,
        exc_info=exc_info,
        extra={
            "request_id": request_id_ctx.get(),
            **kwargs
        }
    )