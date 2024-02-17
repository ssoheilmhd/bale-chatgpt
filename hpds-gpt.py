OPENAI_API_KEY="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"
from openai import OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "please make a shell script which configure nginx as a revrese proxy"}
  ]
)

print(completion.choices[0].message.content)
