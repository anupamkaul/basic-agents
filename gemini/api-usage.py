from google import genai
key_path = '/Users/anupkaul/.key/GEMINI-KEY.txt' 

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

# the client gets the AI key from the env variable 'GEMINI_API_KEY' (with no arguements)
# but here we do https://ai.google.dev/gemini-api/docs/api-key#provide-api-key-explicitly

client = genai.Client(api_key=GEMINI_API_KEY)
print(client)

# usage examples

# text generation
# https://ai.google.dev/gemini-api/docs/text-generation

while True:

    try:
        user_contents = input("\nquery: ")

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            #contents="What is the latest happening on lung cancer research?"
            contents=user_contents
        )

        print(response.text)

    except KeyboardInterrupt:
        print("\nInterrupt detected, exiting loop.")
        break








