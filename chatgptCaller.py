OPENAI_API_KEY="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"
from openai import OpenAI

def SendQuestionToChatgpt(content):
    client = OpenAI(api_key=OPENAI_API_KEY)
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": content}
      ]
    )
    return completion.choices[0].message.content
