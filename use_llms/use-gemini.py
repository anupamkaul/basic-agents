import getpass
import os

if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")

from langchain.chat_models import init_chat_model
model = init_chat_model("gemini_2.0-flash", model_provider="google_genai")

# call the language model by passing a list of messages (by default, the response is a content string)

query = "Hi!"

response = model.invoke( [ {"role": "user", "content" : query} ] )
response.text()
