import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Load environment variables from root .env
load_dotenv()

# 2. Initialize client (points to custom/local endpoint)
client = OpenAI(base_url=os.getenv("URL"), api_key=os.getenv("API_KEY"))

# 3. Define model and chat messages payload
model = "gemini-flash-lite"
role = "user"
prompt = "Who are you?"
message = {
    "role": role,
    "content": prompt,
}
messages = [message]

# 4. Call chat completion API
response = client.chat.completions.create(model=model, messages=messages)

# 5. Extract and print the response text
print(response.choices[0].message.content)
