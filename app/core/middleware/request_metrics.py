# middleware/request_metrics.py

import asyncio
import time

from core.middleware.request_context import request_id_ctx
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


async def save_metrics(data: dict):
    # aquí insertarías en DB
    print("Saving:", data)


class RequestMetricsMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        start_time = time.perf_counter()

        try:
            response = await call_next(request)
            status_code = response.status_code
            return response

        except Exception:
            status_code = 500
            raise

        finally:
            duration = time.perf_counter() - start_time

            request_data = {
                "request_id": request_id_ctx.get(),
                "method": request.method,
                "path": request.url.path,
                "status_code": status_code,
                "duration_ms": round(duration * 1000, 2),
                "client_ip": request.client.host if request.client else None,
            }

            asyncio.create_task(save_metrics(request_data))
