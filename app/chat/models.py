from abc import ABC, abstractmethod
from uuid import UUID

from sqlmodel import SQLModel


class ConversationInputMessage(SQLModel):
    thread_id: UUID
    message: str


class AIService(ABC):
    """Application adapter interface for various AI services"""

    @abstractmethod
    def simple_streaming_conversation(self, message: ConversationInputMessage) -> str:
        raise NotImplementedError()
