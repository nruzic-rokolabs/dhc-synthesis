"""
Connector module providing REST-full HTTP adapter to the application

The module contains:
* fastapi router
* rest controller
"""
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from .dependecies import conversation_service
from .models import ConversationInputMessage
from .service import ConversationService


router = APIRouter()


@router.post("/converse")
def converse(
        message_in: ConversationInputMessage,
        service: ConversationService = Depends(conversation_service)
) -> StreamingResponse:
    return StreamingResponse(content=service.streaming_converse(message_in))
