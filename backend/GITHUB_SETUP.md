# GitHub Repository Setup Guide

This guide explains how to properly set up and deploy your backend to the GitHub repository.

## Repository Structure

The backend repository should have the following structure:

```
backend/
├── api/                 # API route definitions
├── src/                 # Main application source code
│   ├── agents/          # AI agent implementations
│   ├── api/             # API endpoints
│   ├── database/        # Database configuration
│   ├── models/          # Data models
│   ├── services/        # Business logic
│   └── mcp/             # MCP tools
├── tests/               # Test files
├── requirements.txt     # Python dependencies
├── initialize_db.py     # Database initialization script
├── README.md            # Project documentation
├── .env.example         # Example environment variables file
├── .gitignore           # Git ignore file
└── Dockerfile           # Container configuration
```

## Setting Up the Repository

### 1. Initialize the Repository

```bash
# Navigate to your backend directory
cd C:\Users\Dell\Desktop\phase2\backend

# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Todo API Backend with AI Assistant"
```

### 2. Connect to GitHub

```bash
# Add the remote repository
git remote add origin https://github.com/Ayeshaaaqil/backend-phase-2-and-3.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### 3. Create .env.example File

Create a `.env.example` file to show required environment variables:

```env
SECRET_KEY=your-super-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
NEON_DATABASE_URL=postgresql://username:password@ep-wispy-pond-a4mbhory-pooler.us-east-1.aws.neon.tech/dbname?sslmode=require
OPENAI_API_KEY=your-openai-api-key-if-using
```

### 4. Create .gitignore

Create a `.gitignore` file to exclude sensitive and unnecessary files:

```
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.venv/
pip-log.txt
pip-delete-this-directory.txt
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.log
.git/
.mypy_cache/
.pytest_cache/
.hypothesis/

# Environment variables
.env

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
```

### 5. Create Database Initialization Script

I've already created the `initialize_db.py` script that sets up the database tables.

## Deployment Options

### Option 1: Deploy to Hugging Face Spaces (Recommended)

Follow the instructions in the `DEPLOYMENT_GUIDE.md` file to deploy to Hugging Face Spaces.

### Option 2: Deploy to Render

1. Create an account on [Render](https://render.com)
2. Create a new Web Service
3. Connect to your GitHub repository
4. Use the Dockerfile for deployment
5. Add environment variables in the Render dashboard

### Option 3: Deploy to Railway

1. Create an account on [Railway](https://railway.app)
2. Create a new project
3. Connect to your GitHub repository
4. Add environment variables in the Railway dashboard

## Environment Variables

The following environment variables are required for the application:

- `SECRET_KEY`: Secret key for JWT tokens (use a strong random key)
- `ALGORITHM`: Algorithm for JWT (default: HS256)
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Token expiration time (default: 30)
- `NEON_DATABASE_URL`: PostgreSQL connection string for Neon database
- `OPENAI_API_KEY`: OpenAI API key if using OpenAI features

## Running Locally

To run the backend locally:

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up environment variables in a `.env` file

3. Initialize the database:
   ```bash
   python initialize_db.py
   ```

4. Run the application:
   ```bash
   cd src
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

The API will be available at `http://localhost:8000`.

## API Documentation

Once running, you can access the API documentation at:
- `http://localhost:8000/docs` - Interactive API documentation
- `http://localhost:8000/redoc` - Alternative API documentation