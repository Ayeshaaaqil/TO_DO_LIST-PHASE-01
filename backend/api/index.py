# api/index.py
# Vercel Serverless Function for Todo API

import json
from typing import Dict, Any
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import your main FastAPI app
from src.main import app as fastapi_app

# Add CORS middleware for Vercel deployment
fastapi_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create the Mangum adapter for ASGI to serverless compatibility
handler = Mangum(fastapi_app)

# For Vercel serverless functions
def main(event, context):
    return handler(event, context)

# If running locally for testing
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)