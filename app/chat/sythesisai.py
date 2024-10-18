from .models import AIService, ConversationInputMessage


class SynthesisAIService(AIService):

    def simple_streaming_conversation(self, message: ConversationInputMessage) -> str:
        pass
