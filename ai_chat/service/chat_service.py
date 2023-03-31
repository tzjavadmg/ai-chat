from typing import List, Dict
from ai_chat.common.logger import logger
from ai_chat.dao.chat_dao_impl import ChatDaoImpl
from ai_chat.entity.chat import ChatMessage, ChatRole
from ai_chat.openai.openai_api import openai_chat_reply


class ChatService:

    def __init__(self):
        self.__chat_dao = ChatDaoImpl()

    # 获取某个聊天的所有消息
    def get_chat_messages(self, chat_id: int) -> List[Dict]:
        if chat_id is None:
            return []

        chat_messages = self.__chat_dao.get_chat_messages(chat_id)

        messages = [message.get_dict() for message in chat_messages]

        return messages

    # 组装一个简单的消息模型
    """ 
    三条消息：
    system:设置assistant角色和行为。目前实现为取第一条system消息内容
    assistant:保持上下文。目前实现为直接获取最近一条回答内容
    user:本次消息内容
    """

    def get_simple_messages(self, chat_id: int) -> List[Dict]:
        if chat_id is None:
            return []

        chat_roles = [ChatRole.SYSTEM.value, ChatRole.ASSISTANT.value, ChatRole.USER.value]
        messages = []

        for role in chat_roles:
            msg = self.__chat_dao.get_recently_message(chat_id, role)
            if msg is not None:
                messages.append(msg.get_dict())

        return messages

    def save_chat_message(self, user_id: int, role: str, message: str, chat_id: int = None) -> int:
        if chat_id is None:
            topic = message
            if len(topic) > 10:
                topic = topic[0:10]
            chat_id = self.__chat_dao.save_chat(user_id, topic)
            # 把第一句话当作系统消息
            self.__chat_dao.save_chat_message(ChatMessage(ChatRole.SYSTEM.value, message, chat_id))

        self.__chat_dao.save_chat_message(ChatMessage(role, message, chat_id))

        return chat_id

    def chat_reply(self, chat_message: tuple) -> tuple:
        return self.reply(chat_message.get("user_id"), chat_message.get("message"), chat_message.get("chat_id"))

    def reply(self, user_id: int, message: str, chat_id: int = None) -> tuple:

        # 保存消息
        chat_id = self.save_chat_message(user_id, ChatRole.USER.value, message, chat_id)
        #
        messages = self.get_simple_messages(chat_id)
        logger.info("openai api messages: %s", messages)
        # 使用OpenAI应答
        response = openai_chat_reply(messages)
        logger.info("openai api response: %s", response)
        openai_reply = response.choices[0].message.content
        # 记录api 调用日志
        # 记录聊天数据至DB
        self.save_chat_message(
            user_id, ChatRole.ASSISTANT.value, openai_reply, chat_id)

        # print(openai_reply)
        return chat_id, openai_reply

    # 获取某个用户的聊天列表
    def get_chat_list(self, user_id: int):
        pass
