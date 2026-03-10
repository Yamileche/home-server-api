# core/error_models.py
from datetime import datetime


def build_error_payload(request, exc, request_id):
    return {
        "request_id": request_id,
        "path": request.url.path,
        "method": request.method,
        "error_type": type(exc).__name__,
        "message": str(exc),
        "timestamp": datetime.utcnow().isoformat(),
        "client_ip": request.client.host if request.client else None,
    }
