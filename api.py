import os
import json
import secrets
from fastapi import APIRouter, Request, HTTPException, status, Depends
from pydantic import BaseModel
from typing import List
import requests

router = APIRouter()

API_KEYS_FILE = "api_keys.json"

def load_api_keys():
    if not os.path.exists(API_KEYS_FILE):
        return []
    with open(API_KEYS_FILE, "r") as f:
        return json.load(f)

def save_api_keys(keys):
    with open(API_KEYS_FILE, "w") as f:
        json.dump(keys, f)

def create_api_key():
    key = secrets.token_urlsafe(32)
    keys = load_api_keys()
    keys.append(key)
    save_api_keys(keys)
    return key

def validate_api_key(request: Request):
    auth = request.headers.get("Authorization")
    if not auth or not auth.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing or invalid authorization header")
    key = auth.replace("Bearer ", "")
    if key not in load_api_keys():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API key")
    return True

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    model: str
    messages: List[Message]

class Choice(BaseModel):
    index: int
    message: Message
    finish_reason: str = "stop"

class ChatResponse(BaseModel):
    id: str = "chatcmpl-xxx"
    object: str = "chat.completion"
    created: int = 0
    model: str
    choices: List[Choice]

@router.post("/v1/auth/key")
def generate_key():
    key = create_api_key()
    return {"api_key": key}

@router.post("/v1/chat/completions", response_model=ChatResponse)
def chat_completion(request: ChatRequest, valid: bool = Depends(validate_api_key)):
    # Combine user messages for prompt
    prompt = "\n".join([msg.content for msg in request.messages if msg.role == "user"])
    
    # Example: Forward to Jelvan Ai LLM backend (change URL/payload as needed)
    jelvan_ai_url = "http://localhost:11434/api/generate"  # Change to your LLM backend if needed
    payload = {
        "model": request.model,
        "prompt": prompt
    }
    try:
        r = requests.post(jelvan_ai_url, json=payload, timeout=60)
        r.raise_for_status()
        data = r.json()
        llm_reply = data.get("response", "[No response from Jelvan Ai]")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Jelvan Ai backend error: {e}")

    response = ChatResponse(
        model=request.model,
        choices=[
            Choice(
                index=0,
                message=Message(role="assistant", content=llm_reply)
            )
        ]
    )
    return response
