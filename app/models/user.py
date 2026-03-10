import uuid
from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class BaseUser(BaseModel):
    nombre: str
    apellido: str
    email: EmailStr


class GetUser(BaseUser):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)


class CreateUser(BaseModel):
    nombre: str
    apellido: str
    email: EmailStr
    created_at: datetime = Field(default=datetime.now())


class UpdateUser(BaseModel):
    nombre: str | None = None
    apellido: str | None = None
    email: EmailStr
