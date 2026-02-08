---
title: Chatbot Backend
emoji: 💬
colorFrom: indigo
colorTo: green
sdk: docker
app_port: 7860
pinned: false
---

# Chatbot Backend

This is a chatbot backend service built with FastAPI and deployed using Docker on Hugging Face Spaces.

## API Endpoints

- `GET /` - Health check and root endpoint
- `POST /chat` - Chat endpoint that processes user messages
- `GET /health` - Health check endpoint

## Local Development

To run this application locally:

```bash
pip install -r requirements.txt
python app.py
```

The application will be available at `http://localhost:7860`.

## API Usage

Send a POST request to `/chat` with JSON payload:
```json
{
  "message": "Hello, how are you?"
}
```

Response:
```json
{
  "response": "Echo: Hello, how are you?",
  "status": "success"
}
```

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
