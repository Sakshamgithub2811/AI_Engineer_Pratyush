import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user" 

# 3 prompts
prompt1 = "Hii"
prompt2 = "explain time travel in details"
prompt3 = "write a 1000 word essay on machine learning"
prompts=[prompt1,prompt2,prompt3]

for prompt in prompts:
    message={
        "role":role,
        "content":prompt
    }
    messages = [message]

    response=client.chat.completions.create(model=model,messages=messages, max_tokens = 5000)
    usage = response.usage
    print(f"""prompt:{prompt}--> your tokens: {usage.prompt_tokens} completion_token: {usage.completion_tokens} total tokens : {usage.prompt_tokens + usage.completion_tokens}
          finish reason :{response.choices[0].finish_reason}""")
# prompt="Do you know Padho with Pratyush"
# message={
#     "role":role,
#     "content":prompt
# }

# messages=[message]

# print(response)

# answer = response.choices[0].message.content
# print(answer)