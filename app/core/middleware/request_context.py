import uuid
from contextvars import ContextVar

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

request_id_ctx = ContextVar("request_id", default=None)


class RequestIDMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        request_id = str(uuid.uuid4())

        # guardar en contexto
        request_id_ctx.set(request_id)

        response = await call_next(request)

        # opcional: devolver header
        response.headers["X-Request-ID"] = request_id

        return response
