#import dotenv

from dotenv import load_dotenv
load_dotenv(override=True)

import os
openai_api_key = os.getenv('OPENAI_API_KEY') # gets it from local .env here

#print(openai_api_key)

if openai_api_key:
    print(f"My openai key exists and begins {openai_api_key[:8]}")
else:
    print("openai key not set or not found")




