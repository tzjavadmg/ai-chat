from typing import List, Dict

import openai

"""
# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai

openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
主要输入是消息参数。
消息必须是一个消息对象数组，其中每个对象都有一个角色（“system”、“user”或“assistant”）和内容（消息的内容）。

通常，对话首先使用system消息进行格式化，然后是交替的user和assistant消息。

system消息有助于设置assistant的行为。在上面的例子中，assistant被指示“你是一个有用的助手”。

user消息有助于指导assistant。它们可以由应用程序的最终用户生成，或由开发人员设置为指令。

assistant消息帮助存储先前的响应。它们也可以由开发人员编写，以帮助提供所需行为的示例。
"""
openai.api_key = "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"


def openai_chat_reply(messages: List[Dict]):
    # 使用GPT-3模型来回答问题
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
        max_tokens=1000,
        temperature=0,
    )

    return response


"""
{
    'id': 'chatcmpl-6p9XYPYSTTRi0xEviKjjilqrWU2Ve',
    'object': 'chat.completion',
    'created': 1677649420,
    'model': 'gpt-3.5-turbo',
    'usage': {'prompt_tokens': 56, 'completion_tokens': 31, 'total_tokens': 87
    },
    'choices': [
        {
       'message': {
         'role': 'assistant',
         'content': 'The 2020 World Series was played in Arlington, Texas at the Globe Life Field, which was the new home stadium for the Texas Rangers.'
            },
       'finish_reason': 'stop',
       'index': 0
        }
    ]
}

每个回复都将包含一个finish_reason. 的可能值为finish_reason：

stop：API 返回完整的模型输出
length：由于max_tokens参数或令牌限制，模型输出不完整
content_filter：由于我们的内容过滤器中的标记而省略了内容
null: API 响应仍在进行中或不完整
"""
