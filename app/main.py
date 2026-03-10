from core.handlers.exception_handlers import global_exception_handler
from core.logger import logger
from core.middleware.request_context import RequestIDMiddleware
from core.middleware.request_metrics import RequestMetricsMiddleware
from fastapi import FastAPI
from routes import users

app = FastAPI()


@app.get("/")
async def root():
    logger.info("Petición recibida a root", user=123456789)

    return {"message": "root path "}


# Importar rutas
app.include_router(users.router)

# Middleware
app.add_middleware(RequestMetricsMiddleware)
app.add_middleware(RequestIDMiddleware)

# Handlers
app.add_exception_handler(Exception, global_exception_handler)
