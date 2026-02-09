'''
I will use this file as an example of the llm-as-a-judge concept
'''

import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from anthropic import Anthropic

load_dotenv(override=True)

# print the key prefixes to help with any debugging
openai_api_key    = os.getenv('OPENAI_API_KEY')      # chatgpt.com (free) https://platform.openai.com/api-keys ($5 credit to start)
groq_api_key      = os.getenv('GROQ_API_KEY')        # console.groq.com/keys (access llama, gemma etc in fast inference mode) (free)
google_api_key    = os.getenv('GOOGLE_API_KEY')      # https://aistudio.google.com/api-keys<magic-link>  (can always copy)    (free)
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')   # console.anthropic.com (https://platform.claude.com/dashboard) ($5 credit to start)

deepseek_api_key  = os.getenv('DEEPSEEK_API_KEY')    # probably a distilled model; platform.deepseek.com - probably use ollama to run it locally
                                                     # (to avoid any security concerns) - avoid for now, or build an open-weight model yourself and
                                                     # use that...

demosthenes_api_key = os.getenv('DEMOSTHENES-API_KEY')  # setup your infra first ..

print("Hello, llm as judge!")

if openai_api_key:
    print("OPEN AI key exists and begins with: ", openai_api_key[:8])
else:
    print("OPEN AI key not found or does not exist")

if groq_api_key:
    print("GROQ key exists and begins with: ", groq_api_key[:8])
else:
    print("GROQ key not found or does not exist")

if google_api_key:
    print("google key exists and begins with: ", google_api_key[:8])
else:
    print("google key not found or does not exist")

if anthropic_api_key:
    print("anthropic key exists and begins with: ", anthropic_api_key[:8])
else:
    print("anthropic key not found or does not exist")

# currently not using deepseek and demosthenes

# beginning of my first agent..

# first, the input orchestrating code that gathers what to ask every LLM. This itself is not an LLM, just
# human code at this point

request = "Please come up with a challenging, nuanced question that I can ask a number of LLMs to evaluate their intelligence. "
request += "Answer only with the question, no explanation"
messages = [{"role": "user", "content": request}]

print(messages)

# now, ask a standard LLM to generate the question for all LLMs
openai = OpenAI()
response = openai.chat.completions.create(
               model="gpt-5-mini",
               messages=messages,
           )

print("Full response from openAI: ", response, "\n")

question = response.choices[0].message.content
print("Question to ask: ", question)




