import os
import json
import secrets
from fastapi import APIRouter, Request, HTTPException, status, Depends

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

@router.post("/v1/auth/key")
def generate_key():
    key = create_api_key()
    return {"api_key": key}

@router.post("/v1/chat/completions")
def chat_completion(request: Request, valid: bool = Depends(validate_api_key)):
    # Existing logic here, now protected by API key
    return {"message": "Your chat completion logic here."}