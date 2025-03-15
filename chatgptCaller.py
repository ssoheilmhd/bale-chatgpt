from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
openaiAPItoken = os.environ['openaiAPItoken']

def SendQuestionToChatgpt(content):
    """
    This function asks chatgpt your question and gets the answer.
    """
    client = OpenAI(api_key=openaiAPItoken)
    # You can change the chatgpt version here in model
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": content}
      ]
    )
    return completion.choices[0].message.content
