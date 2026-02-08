"""
Simple script to run just the FastAPI backend without Gradio
"""
import uvicorn
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Import your main app
from src.main import app

if __name__ == "__main__":
    print("Starting FastAPI server on http://localhost:8000")
    print("Press Ctrl+C to stop the server")
    uvicorn.run(app, host="127.0.0.1", port=8000)