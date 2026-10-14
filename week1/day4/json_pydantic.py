import json
import os
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel

# ==============================================================================
# 1. Environment & API Client Setup
# ==============================================================================
load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"


# ==============================================================================
# 2. Define Data Schema (Pydantic Model)
# ==============================================================================
class Ticket(BaseModel):
    name: str
    email: str
    issue: str

schema = Ticket.model_json_schema()


# ==============================================================================
# 3. Prepare Prompts & Messages
# ==============================================================================
system_prompt = f"""
Extract the personal information from the ticket strictly based on this schema:
{schema}

If any field is not present in the ticket, return it as null.
Do not add any extra fields in the output.
Do not add any extra text in the output.
Strictly follow the schema and return a valid JSON object.
"""

ticket_text = (
    "Hello my name is saksham . i have an iphone which is not working at all . "
    "my address is delhi . my email is abc@gmail.com and my phone number is 1234567890."
)

user_prompt = f"""
This is a customer ticket. Please extract the personal information from it:
{ticket_text}
"""

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt},
]


# ==============================================================================
# 4. Call LLM with JSON Mode Enforced
# ==============================================================================
response = client.chat.completions.create(
    model=model,
    messages=messages,
    response_format={"type": "json_object"},
)

raw_json = response.choices[0].message.content
print("--- Raw LLM Response (JSON) ---")
print(raw_json)


# ==============================================================================
# 5. Parse JSON & Validate with Pydantic
# ==============================================================================
data = json.loads(raw_json)
ticket = Ticket(**data)

print("\n--- Parsed & Validated Fields ---")
print("Name :", ticket.name)
print("Email:", ticket.email)
print("Issue:", ticket.issue)