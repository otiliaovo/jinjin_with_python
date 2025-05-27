from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
import os


dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
openai_api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key = openai_api_key)

def get_llm_response(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.0,
    )
    response = completion.choices[0].message.content
    return response

prompt = "What is the capital of France?"
response = get_llm_response(prompt)
print(response)