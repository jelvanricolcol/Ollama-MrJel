import os
from fastapi import FastAPI, HTTPException, Header, Depends
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel
import openai
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="MrJel OpenAI API",
    description="API for OpenAI inference with API key authentication",
    version="1.0.0"
)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DEFAULT_MODEL = "gpt-3.5-turbo"
API_KEY = os.getenv("API_KEY", "mrjel-secret")
API_KEY_NAME = "X-API-Key"

if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY not set in environment or .env file.")

openai.api_key = OPENAI_API_KEY

class PromptRequest(BaseModel):
    prompt: str
    model: str = DEFAULT_MODEL

class PromptResponse(BaseModel):
    response: str

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

def get_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API Key")
    return api_key

def prompt_openai(prompt: str, model: str = DEFAULT_MODEL) -> str:
    try:
        completion = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OpenAI error: {e}")

@app.post("/generate", response_model=PromptResponse, dependencies=[Depends(get_api_key)])
def generate(req: PromptRequest):
    result = prompt_openai(req.prompt, req.model)
    return PromptResponse(response=result)