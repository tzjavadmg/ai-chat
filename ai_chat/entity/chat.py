from typing import List
from enum import Enum, unique


class ChatMessage:
    def __init__(self, role: str, content: str, chat_id: int = None, _id: int = None):
        self.__chat_id = chat_id
        self.__role = role
        self.__content = content
        self.__id = _id

    def get_dict(self):
        return {"role": self.__role, "content": self.__content}

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, _id: int):
        self.__id = _id

    @property
    def chat_id(self) -> int:
        return self.__chat_id

    @chat_id.setter
    def chat_id(self, chat_id: int):
        self.__chat_id = chat_id

    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, role: str):
        self.__role = role

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content


class Chat:
    def __init__(self, user_id: int, topic: str, messages: List[ChatMessage] = None, _id: int = None):
        self.__user_id = user_id
        self.__topic = topic
        self.__messages = messages
        self.__id = _id

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, _id):
        self.__id = _id

    @property
    def user_id(self) -> int:
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id: int):
        self.__user_id = user_id

    @property
    def topic(self) -> str:
        return self.__topic

    @topic.setter
    def topic(self, topic):
        self.__topic = topic

    @property
    def messages(self) -> List[ChatMessage]:
        return self.__messages

    @messages.setter
    def messages(self, messages):
        self.__messages = messages


# 使用@unique装饰器确保枚举常量值唯一
@unique
class ChatRole(Enum):
    USER = "user"
    SYSTEM = "system"
    ASSISTANT = "assistant"
