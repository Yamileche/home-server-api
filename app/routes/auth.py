from fastapi import APIRouter
from fastapi.requests import Request

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
async def login(request: Request): ...
