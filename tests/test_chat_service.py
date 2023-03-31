from ai_chat.common.logger import logger
import unittest

from ai_chat.entity.chat import ChatRole
from ai_chat.service.chat_service import ChatService


class TestChatService(unittest.TestCase):
    def setUp(self):
        self._chat_service = ChatService()

    def test_get_chat_messages(self):
        messages = self._chat_service.get_chat_messages(1)
        for message in messages:
            print("消息内容：%s", message)

    def test_save_chat_message(self):
        self._chat_service.save_chat_message(1, ChatRole.USER.value, "python真的很容易")

    def test_reply(self):
        question = "我想让你扮演一个go语言专家，接下来我们的聊天都是和go相关的"
        chat_id, answer = self._chat_service.reply(1, question)
        logger.info("Q:%s", question)
        logger.info("A:%s", answer)

        question = "我要开始提问了，你先介绍一下自己"
        answer = self._chat_service.reply(1, question, chat_id)
        logger.info("Q:%s", question)
        logger.info("A:%s", answer)

        question = "请帮我编写一个快速排序算法"
        answer = self._chat_service.reply(1, question, chat_id)
        logger.info("Q:%s", question)
        logger.info("A:%s", answer)
