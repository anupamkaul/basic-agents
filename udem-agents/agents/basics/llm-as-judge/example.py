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

# (1) first, the input orchestrating code that gathers what to ask every LLM. This itself is not an LLM, just
# human code at this point

request = "Please come up with a challenging, nuanced question that I can ask a number of LLMs to evaluate their intelligence. "
request += "Answer only with the question, no explanation"
messages = [{"role": "user", "content": request}]

print(messages)

# (2) now, ask a standard LLM to generate the question for all LLMs
openai = OpenAI()
response = openai.chat.completions.create(
               model="gpt-5-mini",
               messages=messages,
           )

print("Full response from openAI: ", response, "\n")

question = response.choices[0].message.content
print("Question to ask: ", question)

# (3) now we route the same question to all LLMs that are to be judged. Doing this sequentially but
# this could also be parallelized via multiple threads, multiple CPUs or boxes, etc

competitors = []
answers     = []
messages = [{"role": "user", "content": question}]

# start..

# The API we know well
# I've updated this with the latest model, but it can take some time because it likes to think!
# Replace the model with gpt-4.1-mini if prefer not to wait 1-2 mins

model_name = "gpt-5-nano"
print("Asking ", model_name, "...\n")

response = openai.chat.completions.create(model=model_name, messages=messages)
answer = response.choices[0].message.content

print("Answer from ", model_name, ": ", answer)
competitors.append(model_name)
answers.append(answer)

# Anthropic has a slightly different API, and Max Tokens is required

model_name = "claude-sonnet-4-5"
print("Asking ", model_name, "...\n")

claude = Anthropic()
response = claude.messages.create(model=model_name, messages=messages, max_tokens=1000)
answer = response.content[0].text

print("Answer from ", model_name, ": ", answer)
competitors.append(model_name)
answers.append(answer)

# Google gemini now

gemini = OpenAI(api_key=google_api_key, base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
model_name = "gemini-2.5-flash"
print("Asking ", model_name, "...\n")

response = gemini.chat.completions.create(model=model_name, messages=messages)
answer = response.choices[0].message.content

print("Answer from ", model_name, ": ", answer)
competitors.append(model_name)
answers.append(answer)

# Use GROQ to query the latest OSS from openAI as another LLM..

groq = OpenAI(api_key=groq_api_key, base_url="https://api.groq.com/openai/v1")
model_name = "openai/gpt-oss-120b"
print("Asking ", model_name, "...\n")

response = groq.chat.completions.create(model=model_name, messages=messages)
answer = response.choices[0].message.content

print("Answer from ", model_name, ": ", answer)
competitors.append(model_name)
answers.append(answer)

# (4) : prepare the input to be judged..
 
# 4.a done and collected answers, now zip them together to judge them..

for competitor, answer in zip(competitors, answers): # see, zip.txt
    print(f"Competitor: {competitor}\n\n{answer}")

# 4.b Let's bring this together, using enumerate

# 'together' is going to pull in the material to be judged as a mega prompt
# to the final LLM I choose to be the judge..

together = ""

for index, answer in enumerate(answers):
    together += f"# Response from competitor {index+1}\n\n"
    together += answer + "\n\n"

print("together: ", together)

# 4.c now create the judging input message prompt for the LLM as judge

judge = f"""You are judging a competition between {len(competitors)} competitors.
Each model has been given this question:

{question}

Your job is to evaluate each response for clarity and strength of argument, and rank them in order of best to worst.
Respond with JSON, and only JSON, with the following format:
{{"results": ["best competitor number", "second best competitor number", "third best competitor number", ...]}}

Here are the responses from each competitor:

{together}

Now respond with the JSON with the ranked order of the competitors, nothing else. Do not include markdown formatting or code blocks."""

print("Input message for judge: ", judge)

# 4.d create the judge message prompt

judge_messages = [{"role": "user", "content": judge}]

# 5 .. and now, lets judge ! 

openai = OpenAI()
response = openai.chat.completions.create(
    model="gpt-5-mini",
    messages=judge_messages,
)
results = response.choices[0].message.content
print(results)

# OK let's turn this into results!

results_dict = json.loads(results)
ranks = results_dict["results"]

for index, result in enumerate(ranks):
    competitor = competitors[int(result)-1]
    print(f"Rank {index+1}: {competitor}") 

