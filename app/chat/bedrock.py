from .models import AIService, ConversationInputMessage


class BedrockAIService(AIService):

    def simple_streaming_conversation(self, message: ConversationInputMessage) -> str:
        pass

