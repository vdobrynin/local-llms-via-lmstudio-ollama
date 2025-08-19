from openai import OpenAI

client = OpenAI(
  base_url="http://localhost:11434/v1",
  api_key="something-doesn't-matter",
)

response = client.chat.completions.create(
  model="google/gemma-3-27b",
  messages=[
    {
      "role": "system",
      "content": "You are a helpful and friendly assistant."
    },
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ],
  temperature=0.7,
)

print(response.choices[0].message.content)