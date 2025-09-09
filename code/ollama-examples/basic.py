from openai import OpenAI

client = OpenAI(
  base_url="http://localhost:11434/v1",
  api_key="something-doesn't-matter",
)

response = client.chat.completions.create(
  model="qwen3:32b-q4_K_M",
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