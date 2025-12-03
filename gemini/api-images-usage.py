from google import genai
from google.genai import types
from PIL import Image

key_path = '/home/anupam/.key/GEMINI-KEY.txt' 
try:
    with open(key_path, 'r', encoding='utf-8') as file:
        GEMINI_API_KEY = file.read()
        GEMINI_API_KEY = GEMINI_API_KEY.rstrip('\n')

    print("File content read successfully:")
    #print("My GEMINI Key: ", GEMINI_API_KEY)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

client = genai.Client(api_key=GEMINI_API_KEY)
print(client)

prompt = (
    "Create a picture of a cat eating a pineapple  dish in a fancy restaurant with a Gemini theme"
)

response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents=[prompt],
)

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = part.as_image()
        image.save("generated_image.png")
