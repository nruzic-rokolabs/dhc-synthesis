"""
Connector module providing REST-full HTTP adapter to the application for IND document related functionality

The module contains:
* fastapi router
* rest controller
* controller level models (aka. schemas), like pydantic request and response models
"""
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_ind_document_list():
    return {"message": "No INDs at the moment!"}
