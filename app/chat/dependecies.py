from .openai import OpenAIService
from .service import ConversationService


def conversation_service() -> ConversationService:
    return ConversationService(
        ai_service=OpenAIService()
    )
