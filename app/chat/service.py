from .models import ConversationInputMessage, AIService


class ConversationService:

    def __init__(self, ai_service: AIService):
        self.ai_service = ai_service

    def streaming_converse(self, message: ConversationInputMessage) -> str:
        # If user in appropriate role...
        # And we want to do simple chat
        for chunk in self.ai_service.simple_streaming_conversation(message):
            yield chunk
