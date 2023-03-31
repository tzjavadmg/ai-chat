from typing import List, Optional

from ai_chat.dao.chat_dao import ChatDao
from ai_chat.dao.conn_pool import open_cursor
from ai_chat.entity.chat import Chat, ChatMessage, ChatRole


class ChatDaoImpl(ChatDao):

    def get_recently_message(self, chat_id: int, role: str = ChatRole.USER.value) -> Optional[ChatMessage]:
        query = """
                SELECT *
                FROM chat_message
                WHERE chat_id = %s AND role = %s
                ORDER BY id DESC
                LIMIT 1
            """

        values = (chat_id, role)

        with open_cursor() as cursor:
            cursor.execute(query, values)
            row = cursor.fetchone()

        if row is None:
            return None

        return ChatMessage(row["role"], row["content"])

    def save_chat(self, user_id: int, topic: str) -> int:
        query = "INSERT INTO chat(user_id,topic) VALUES ( %s, %s)"
        values = (user_id, topic)

        with open_cursor() as cursor:
            # 插入聊天表
            cursor.execute(query, values)
            # 获取插入记录的主键ID
            return cursor.lastrowid

    def save_chat_message(self, message: ChatMessage) -> int:
        query = "INSERT INTO chat_message(chat_id,role,content) VALUES (%s, %s, %s)"
        values = (message.chat_id,
                  message.role,
                  message.content)

        with open_cursor() as cursor:
            cursor.execute(query, values)
            # 获取插入记录的主键ID
            return cursor.lastrowid

    def get_chat(self, chat_id: int) -> Optional[Chat]:
        messages: List[ChatMessage] = self.get_chat_messages(chat_id)
        query = "SELECT * FROM chat where id= %s"
        values = (chat_id,)

        with open_cursor() as cursor:
            cursor.execute(query, values)
            row = cursor.fetchone()

        if row is None:
            return None

        return Chat(row["user_id"], row["topic"], messages, row["id"])

    def get_chat_messages(self, chat_id: int) -> List[ChatMessage]:
        query = "SELECT * FROM chat_message where chat_id= %s"
        values = (chat_id,)

        with open_cursor() as cursor:
            cursor.execute(query, values)
            rows = cursor.fetchall()

        return [
            ChatMessage(
                _id=row["id"],
                chat_id=row["chat_id"],
                role=row["role"],
                content=row["content"],
            )
            for row in rows
        ]
