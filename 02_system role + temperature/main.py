import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Load environment variables from root .env
load_dotenv()

# 2. Initialize client
client = OpenAI(base_url=os.getenv("URL"), api_key=os.getenv("API_KEY"))

# 3. System role (defines AI behavior/persona) & User prompt
messages = [
    {
        "role": "system",
        "content": "You are a concise AI tutor. Explain concepts in 2 sentences.",
    },
    {
        "role": "user",
        "content": "What is temperature in LLMs?",
    },
]

# 4. Call chat completion API
# temperature: 0.0 = deterministic/focused, 1.0+ = creative/exploratory
response = client.chat.completions.create(
    model="gemini-flash-lite",
    messages=messages,
    temperature=0.3,
)

# 5. Extract and print the response text
print(response.choices[0].message.content)
