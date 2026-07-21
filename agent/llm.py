# agent/llm.py

from openai import OpenAI
class LLM:
    def __init__(self):
        self.client = OpenAI(
            api_key="sk-7d4301dee35043709cc458feca94dfb1",
            base_url="https://api.deepseek.com"
        )
    def generate(self, prompt):
        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role":"system",
                    "content":
                    "你是一名环境污染隐患排查专家"
                },
                {
                    "role":"user",
                    "content":prompt
                }
            ],
            temperature=0.2
        )
        return response.choices[0].message.content