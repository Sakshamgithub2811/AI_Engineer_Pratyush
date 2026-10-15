import os
import sys
from pathlib import Path
from time import sleep
from dotenv import load_dotenv, find_dotenv
from groq import Groq

# Support emojis and special Unicode characters in Windows terminal
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')



# ==============================================================================
# 1. Environment & API Client Setup
# ==============================================================================
load_dotenv(find_dotenv())
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"

prompt=" explain the internet"
message={
    "role":"user",
    "content": prompt
}

messages = [message]
# response = client.chat.completions.create(model=model, messages=messages)
# answer = response.choices[0].message.content
# print(answer)

stream = client.chat.completions.create(model=model, messages=messages, stream=True)
for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)


