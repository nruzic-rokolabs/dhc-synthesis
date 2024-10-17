"""
Connector module providing REST-full HTTP adapter to the application

The module contains:
* fastapi router
* rest controller
* controller level models (aka. schemas), like pydantic request and response models
"""
from fastapi import APIRouter

from app import service
from app.domain import Greeting

router = APIRouter()


@router.get("/")
def hello(name: str) -> str:
    greeting: Greeting = service.get_greeting(name)
    return greeting.hello()
