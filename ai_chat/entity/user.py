from typing import List
from dataclasses import dataclass
from ai_chat.entity.chat import Chat


@dataclass
class User:
    name: int
    password: str
    id: int = None
    nick_name: str = None
    avatar: str = None
    chats: List[Chat] = None
