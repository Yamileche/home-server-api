import logging
from core.middleware.request_context import request_id_ctx

class RequestIdFilter(logging.Filter):
    def filter(self, record):
        record.request_id = request_id_ctx.get() or "-"
        return True