import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv(override=True)


@dataclass
class Settings:
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
