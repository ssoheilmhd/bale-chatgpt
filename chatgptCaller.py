from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
baleAPItoken = os.environ['baleAPItoken']

def SendQuestionToChatgpt(content):
    client = OpenAI(api_key=baleAPItoken)
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": content}
      ]
    )
    return completion.choices[0].message.content
