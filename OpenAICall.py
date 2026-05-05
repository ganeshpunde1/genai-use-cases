from openai import OpenAI

import os
os.environ["OPENAI_API_KEY"] = "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"  # your new key
# print( os.getenv("OPENAI_API_KEY") )

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # use your new regenerated key

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "write a haiku about ai"}]
)

print(response.choices[0].message.content)
