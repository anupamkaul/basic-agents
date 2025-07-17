from openai import OpenAI
#key_path = './OPENAI-KEY.txt' 
key_path = '/Users/anupkaul/.key//OPENAI-KEY.txt' 

try:
    with open(key_path, 'r', encoding='utf-8') as file:
        OPENAI_API_KEY = file.read()
        OPENAI_API_KEY = OPENAI_API_KEY.rstrip('\n')

    print("File content read successfully:")
    #print("My openAI Key: ", OPENAI_API_KEY)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

client = OpenAI(api_key=OPENAI_API_KEY)
print(client)

system_message = """
You are a professional researcher preparing a structured, data-driven report on behalf of a global health economics team. Your task is to analyze the health question the user poses.

Do:
- Focus on data-rich insights: include specific figures, trends, statistics, and measurable outcomes (e.g., reduction in hospitalization costs, market size, pricing trends, payer adoption).
- When appropriate, summarize data in a way that could be turned into charts or tables, and call this out in the response (e.g., “this would work well as a bar chart comparing per-patient costs across regions”).
- Prioritize reliable, up-to-date sources: peer-reviewed research, health organizations (e.g., WHO, CDC), regulatory agencies, or pharmaceutical earnings reports.
- Include inline citations and return all source metadata.

Be analytical, avoid generalities, and ensure that each section supports data-backed reasoning that could inform healthcare policy or financial modeling.
"""

#print(system_message)

user_query = "Research the economic impact of semaglutide on global healthcare systems"

response = client.responses.create(
model="o3-deep-research",
  input=[
    {
      "role": "developer",
      "content": [
        {
          "type": "input_text",
          "text": system_message,
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "input_text",
          "text": user_query,
        }
      ]
    }
  ],
  reasoning={
    "summary": "auto"
  },
  tools=[
    {
      "type": "web_search_preview"
    },
    {
      "type": "code_interpreter",
      "container": {
        "type": "auto",
        "file_ids": []
      }
    }
  ]
)

# need to setup paid account








