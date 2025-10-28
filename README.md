# Ollama-MrJel

Open source starter for building AI-powered apps with OpenAI API in Python.

## Features

- OpenAI GPT (or other) LLMs
- Python sample code for sending prompts to OpenAI
- **Web API** using FastAPI for programmatic access
- **Dynamic API Key authentication** (users generate their own keys)
- Docker support
- MIT licensed

## API Key Generation & Usage

To use this API, you need an API key. You can generate your own key and use it to authenticate your requests.

### 1. Generate an API Key

**Endpoint:**  
`POST /v1/auth/key`

**Request Example:**
```bash
curl -X POST http://localhost:8000/v1/auth/key
```
**Response:**
```json
{
  "api_key": "your-generated-api-key"
}
```

### 2. Authenticate Your Requests

Include your API key in the `Authorization` header using the `Bearer` scheme:

```bash
curl -H "Authorization: Bearer your-generated-api-key" \
     -X POST http://localhost:8000/v1/chat/completions \
     -d '{ "model": "gpt-3.5-turbo", "messages": [ ... ] }'
```

All major endpoints require a valid API key.

### 3. Example: Using with n8n

- Use the n8n HTTP Request node.
- Set the Authorization header as shown above.
- Use the appropriate endpoint (e.g., `/v1/chat/completions`) and match OpenAI’s payload format.

### 4. Available Endpoints

- `/v1/auth/key` — Generate a new API key
- `/v1/chat/completions` — Chat endpoint (OpenAI-compatible)
- ... (add more as needed)

## Quick Start

### Prerequisites

- Python 3.8+
- (Optional) Docker installed

### Run Locally

1. Clone the repository:

    ```sh
    git clone https://github.com/jelvanricolcol/Ollama-MrJel.git
    cd Ollama-MrJel
    ```

2. (Optional) Copy `.env.example` to `.env` if using OpenAI backend:

    ```sh
    cp .env.example .env
    # Edit .env to set your OPENAI_API_KEY
    ```

3. Install Python dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Run the API server:

    ```sh
    uvicorn main:app --reload
    ```

5. Generate your API key and use it for all requests (see above).

6. Visit [http://localhost:8000/docs](http://localhost:8000/docs) and "Authorize" with your API key to try out the endpoints.

### Run with Docker

1. Build and start the container:

    ```sh
    docker build -t mrjel-openai .
    docker run --env OPENAI_API_KEY=sk-xxx -p 8000:8000 mrjel-openai
    ```

2. The API will be at [http://localhost:8000/docs](http://localhost:8000/docs).

## Project Structure

- `api.py` — FastAPI web API for OpenAI prompts and key management
- `main.py` — CLI sample or FastAPI app entrypoint
- `requirements.txt` — Python dependencies
- `Dockerfile` — Container setup
- `.env.example` — Example environment file
- `LICENSE` — MIT license

## API Usage

- **POST /v1/chat/completions**
    - Header: `Authorization: Bearer <your-generated-api-key>`
    - Request JSON:  
      ```json
      { "model": "gpt-3.5-turbo", "messages": [ ... ] }
      ```
    - Response JSON:  
      ```json
      { "message": "Your chat completion logic here." }
      ```
- Try it live at `/docs` after you start the API!

## Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

MIT License. © 2025 Jelvan Ricolcol