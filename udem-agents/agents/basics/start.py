'''
Simply test that envs, API keys and instantiating LLM classes work
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
print(openai) # just a pointer, not that it matters much

# create a list of messages in familiar openAI format

my_messages = [{"role": "user", "content": "what is 2+3"}]
response = openai.chat.completions.create(
            model="gpt-4.1-nano",
            messages=my_messages
        )
print(response.choices[0].message.content)

# now let's change the model to a cheaper one, ask it to ask a difficult question
# and then have it answer its question itself:

question = "Please propose a hard, challenging question to assess someone's IQ. Respond only with the question."
my_messages = [{"role": "user", "content": question}]

# ask it - this uses GPT 4.1 mini, still cheap but more powerful than nano
response = openai.chat.completions.create(
    model="gpt-4.1-mini",
    messages=my_messages
)

question = response.choices[0].message.content
print(question)

# now let it answer its own hard question :) 
my_messages = [{"role": "user", "content": question}]
response = openai.chat.completions.create(
    model="gpt-4.1-mini",
    messages=my_messages
)

answer = response.choices[0].message.content
print(answer)

