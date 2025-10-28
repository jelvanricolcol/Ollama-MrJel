# Ollama-MrJel

Open source starter for building AI-powered apps with OpenAI API in Python.

## Features

- OpenAI GPT (or other) LLMs
- Python sample code for sending prompts to OpenAI
- **Web API** using FastAPI for programmatic access
- **API Key authentication** (set via environment variable)
- Docker support
- MIT licensed

## Quick Start

### Prerequisites

- Python 3.8+
- [OpenAI account & API key](https://platform.openai.com/account/api-keys)
- (Optional) Docker installed

### Run Locally

1. Clone the repository:

    ```sh
    git clone https://github.com/jelvanricolcol/Ollama-MrJel.git
    cd Ollama-MrJel
    ```

2. Copy `.env.example` to `.env` and add your OpenAI API key:

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
    uvicorn api:app --reload
    ```

5. All requests must include your API key (default: `mrjel-secret`):

    ```
    X-API-Key: mrjel-secret
    ```

6. Visit [http://localhost:8000/docs](http://localhost:8000/docs) and "Authorize" with the API key to try out the endpoints.

### Run with Docker

1. Build and start the container:

    ```sh
    docker build -t mrjel-openai .
    docker run --env OPENAI_API_KEY=sk-xxx --env API_KEY=your-secret-key -p 8000:8000 mrjel-openai
    ```

2. The API will be at [http://localhost:8000/docs](http://localhost:8000/docs).

## Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key.
- `API_KEY`: Key required in `X-API-Key` header for all API requests (default: `mrjel-secret`).

## Project Structure

- `api.py` — FastAPI web API for OpenAI prompts
- `main.py` — CLI sample for direct OpenAI prompt
- `requirements.txt` — Python dependencies
- `Dockerfile` — Container setup
- `.env.example` — Example environment file
- `LICENSE` — MIT license

## API Usage

- **POST /generate**
    - Header: `X-API-Key: mrjel-secret`
    - Request JSON:  
      ```json
      { "prompt": "Hello, world!", "model": "gpt-3.5-turbo" }
      ```
    - Response JSON:  
      ```json
      { "response": "OpenAI's answer..." }
      ```
- Try it live at `/docs` after you start the API!

## Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

MIT License. © 2025 Jelvan Ricolcol