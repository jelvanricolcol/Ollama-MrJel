import os
import openai
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = "gpt-3.5-turbo"  # You can change to gpt-4, etc.

if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY not set in environment or .env file.")

openai.api_key = OPENAI_API_KEY

def prompt_openai(prompt, model=MODEL_NAME):
    completion = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content.strip()

if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Sending to OpenAI...")
    response = prompt_openai(user_prompt)
    print("OpenAI says:", response)