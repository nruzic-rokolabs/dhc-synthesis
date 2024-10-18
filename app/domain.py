"""
Domain module from Domain Driven Design.

The module contains models, services, and utilities related to the business problem domain.
"""
from datetime import datetime

from pydantic import BaseModel

from .settings import settings


class Greeting(BaseModel):
    timestamp: datetime = datetime.utcnow()
    name: str

    def hello(self) -> str:
        return f"Hello {self.name}! This is {settings.application_name}. Today is '{self.timestamp}'."
