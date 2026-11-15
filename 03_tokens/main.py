"""
=============================================================================
TOKEN CONCEPT & CALCULATION (QUICK REVISION)
=============================================================================
1. What is a Token?
   - LLMs do NOT read full words or raw characters; they break text into
     sub-word chunks called "tokens" using a tokenizer (e.g., BPE).
   - A token can be a single character, part of a word, or a full word.

2. Rough Rules of Thumb (English text):
   - 1 token  ≈ 4 characters
   - 1 token  ≈ 0.75 words  (100 tokens ≈ 75 words)
   - Common words = 1 token (e.g., "the", " world", " apple")
   - Rare/complex words, code, or other languages are split into sub-tokens:
     e.g., "tokenization" -> ["token", "ization"] (2 tokens)

3. How Token Usage is Calculated:
   - prompt_tokens     : Your input (role names, prompt text, formatting overhead).
   - completion_tokens : What the model generates.
   - total_tokens      : prompt_tokens + completion_tokens (determines API cost & context limit).

4. max_tokens & finish_reason:
   - max_tokens caps ONLY the completion_tokens (output length).
   - finish_reason == "stop"   -> Model naturally concluded before the limit.
   - finish_reason == "length" -> Model was forcefully cut off by max_tokens.
=============================================================================
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Load environment and initialize client
load_dotenv()
client = OpenAI(base_url=os.getenv("URL"), api_key=os.getenv("API_KEY"))

model = "gemini-auto"
role = "user"

# 2. Prompts of varying lengths to observe token usage & truncation
prompts = [
    "Hi!",                                              # Short prompt (finishes under limit)
    "Explain time travel in Detail but under 100 words", # Medium prompt
    "Write a 1000 word essay on Machine learning",       # Long prompt (will exceed limit)
]

for prompt in prompts:
    messages = [{"role": role, "content": prompt}]

    # 3. max_tokens caps output length (hard stop on generation)
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=50,
    )
    usage = response.usage

    # 4. Token metrics & finish_reason:
    # - "stop": completed naturally under the limit
    # - "length": cut off because it reached max_tokens
    print(
        f"Prompt: {prompt} --> "
        f"your tokens: {usage.prompt_tokens} | "
        f"completion_tokens: {usage.completion_tokens} | "
        f"total tokens: {usage.total_tokens} | "
        f"Finish Reason: {response.choices[0].finish_reason}"
    )

