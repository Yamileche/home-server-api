from fastapi import Request
from fastapi.responses import JSONResponse
from core.middleware.request_context import request_id_ctx
from core.logger import logger


async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Error: {exc}",exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "error": "INTERNAL_SERVER_ERROR",
            "message": str(exc),
            "request_id": request_id_ctx.get(),
        },
    )