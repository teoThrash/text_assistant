import openai
import json

openai.api_key = "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"

with open('seed.json', 'r') as file:
    messages = json.load(file)

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
  )
response_text = response["choices"][0]["message"]["content"]
print(response_text)
# In user prompt change based on input what the story contains