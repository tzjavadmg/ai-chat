from typing import Union
from ai_chat.common.logger import logger
import socketio
from fastapi import FastAPI, Depends

from ai_chat.service.chat_service import ChatService

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
app = FastAPI()
socketio_app = socketio.ASGIApp(sio, app)
chat_service = ChatService()


# 定义Socket.IO事件处理器
@sio.event
async def message(sid: str, data: tuple):
    logger.info("client message: %s, %s", sid, data)
    if "user_id" not in data:
        data["user_id"] = hash(sid)
    chat_id, chat_message = chat_service.chat_reply(data)
    logger.info("server message: %s, %s", chat_id, chat_message)
    await sio.emit('message', dict(chat_id=chat_id, message=chat_message), room=sid)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
