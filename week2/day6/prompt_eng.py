import json
import os
import sys
from dotenv import load_dotenv
from groq import Groq

sys.stdout.reconfigure(encoding="utf-8")

# ==============================================================================
# 1. Environment & API Client Setup
# ==============================================================================
load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"

def llm_ans(prompt):
    message = {
            "role":"user",
            "content":prompt
    }
    messages = [message]
    response = client.chat.completions.create(model=model, messages = messages)
    ans = response.choices[0].message.content
    return ans

bad_prompt = """
#ROLE:
you are a support assistant at a mobile/laptop company 
#TASK:
you have to classify the issue in a category
#CONSTRAINT 
you have to classigy the issue in one of the    category namely billing , technical, return 
#OUTPUT FORMAT
your answer should be in one word only. The one word should be one of the following constraints
#Examples
user: my laptop is not working 
AI: technical
user: i am not happy with my laptop 
AI: return
user: my bill is too high 
AI: billing
#FALLBACK
if the issue is unrelated to any of the categories mentioned in constraints , then the answe should be other 
this is a user complaint:
friend girlfriend left 
"""    
print(llm_ans(bad_prompt))