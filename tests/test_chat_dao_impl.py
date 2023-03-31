from unittest import TestCase
from ai_chat.common.logger import logger

from ai_chat.dao.chat_dao_impl import ChatDaoImpl
from ai_chat.entity.chat import ChatMessage, ChatRole


class TestChatDaoImpl(TestCase):
    def setUp(self):
        self._chat_dao = ChatDaoImpl()

    def test_save_chat(self):
        chat_id = self._chat_dao.save_chat(user_id=1,
                                           topic="python学习")

        self.assertTrue(chat_id is not None, "save_chat test failed")

    def test_save_chat_message(self):
        chat_id = self._chat_dao.save_chat(user_id=1,
                                           topic="python学习")

        self._chat_dao.save_chat_message(ChatMessage(chat_id=chat_id, role="system",
                                                     content="你是一个python专家,接下来你需要帮助我学习python"))

        self._chat_dao.save_chat_message(
            ChatMessage(chat_id=chat_id, role="user", content="如何定义一个空元组"))

        self.assertTrue(chat_id is not None, "save_chat_message test failed")

    def test_get_chat(self):
        chat = self._chat_dao.get_chat(1)
        logger.info("标题：%s", chat.topic)
        for message in chat.messages:
            logger.info(message.content)

        self.assertEqual(chat.id, 1, "get_chat test failed")

    def test_get_chat_messages(self):
        for message in self._chat_dao.get_chat_messages(1):
            print(message.content)

    def test_get_recently_message(self):
        # m1 = self._chat_dao.get_recently_message(4, ChatRole.SYSTEM.value)
        # print(vars(m1))

        m2 = self._chat_dao.get_recently_message(4, ChatRole.USER.value)
        print(vars(m2))

        m3 = self._chat_dao.get_recently_message(4, ChatRole.ASSISTANT.value)
        print(vars(m3))
