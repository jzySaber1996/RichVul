# This code is Apache 2 licensed:
# https://www.apache.org/licenses/LICENSE-2.0
import openai
import os
from src_IR_prediction import Config as cf
os.environ["http_proxy"]="127.0.0.1:7890"
os.environ["https_proxy"]="127.0.0.1:7890"

openai.api_key = cf.api_key


class ChatBot:
    def __init__(self, system=""):
        self.system = system
        self.messages = []
        if self.system:
            self.messages.append({"role": "system", "content": system})

    def __call__(self, message):
        self.messages.append({"role": "user", "content": message})
        result = self.execute()
        self.messages.append({"role": "assistant", "content": result})
        return result

    def execute(self):
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=self.messages)
        # Uncomment this to print out token usage each time, e.g.
        # {"completion_tokens": 86, "prompt_tokens": 26, "total_tokens": 112}
        # print(completion.usage)
        return completion.choices[0].message.content
