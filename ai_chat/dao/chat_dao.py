from abc import ABC, abstractmethod
from typing import List
from ai_chat.entity.chat import Chat, ChatMessage, ChatRole


class ChatDao(ABC):

    @abstractmethod
    def save_chat(self, user_id: int, topic: str) -> int:
        pass

    @abstractmethod
    def save_chat_message(self, chat: ChatMessage) -> int:
        pass

    @abstractmethod
    def get_chat(self, chat_id: int) -> Chat:
        pass

    @abstractmethod
    def get_chat_messages(self, chat_id: int) -> List[ChatMessage]:
        pass

    @abstractmethod
    def get_recently_message(self, chat_id: int, role: str = ChatRole.USER.value) -> ChatMessage:
        pass
