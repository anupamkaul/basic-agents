'''
Ask openAI where agentic solutions could be applied for business (ask it to solve) 
'''

from dotenv import load_dotenv
load_dotenv(override=True)

import os
openai_api_key = os.getenv('OPENAI_API_KEY') # gets it from local .env here

if openai_api_key:
    print(f"My openai key exists and begins {openai_api_key[:8]}")
else:
    print("openai key not set or not found")


from openai import OpenAI # create an instance of openAI's client class
openai = OpenAI(api_key=openai_api_key)

'''
Now I will ask it a business question where Agentic AI can be useful
Then I will ask it to present a pain point in that industry
And finally a solution with agents

'''
# 1 
my_messages = [{"role": "user", "content": "Pick up a business area that might be worth exploring for an agentic AI opportunity. Your answer should size up the opportunity in terms of TAM (total addressable market) with a high level analysis"}]

response = openai.chat.completions.create(
    model="gpt-4.1-mini",
    messages=my_messages
)

answer = response.choices[0].message.content
print(answer)


# 2 
my_messages = [{"role": "user", "content": "From the previous response, present a pain point in this industry - something challenging that might be ripe for an agentic solution. Remember the pain point as I will ask about it later"}]

response = openai.chat.completions.create(
    model="gpt-4.1-mini",
    messages=my_messages
)

answer = response.choices[0].message.content
print(answer)


# 3 
my_messages = [{"role": "user", "content": "Now propose an agentic solution in detail that can address the previous pain point"}]

response = openai.chat.completions.create(
    model="gpt-4.1-mini",
    messages=my_messages
)

answer = response.choices[0].message.content
print(answer)

