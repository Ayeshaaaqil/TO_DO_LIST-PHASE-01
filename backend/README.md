# Todo API Backend with AI Assistant

This is a backend API for a Todo application with AI-powered task management capabilities. The API is built with FastAPI and includes authentication, todo management, and an AI assistant that understands natural language commands.

## Features

- **User Authentication**: Secure signup and signin with JWT tokens
- **Todo Management**: Full CRUD operations for managing tasks
- **AI Assistant**: Natural language processing for todo management
- **Database Integration**: PostgreSQL/Neon database with SQLModel ORM
- **Real-time Chat**: Interactive chat interface for AI assistant

## Tech Stack

- **Framework**: FastAPI
- **Database**: SQLModel (SQLAlchemy + Pydantic)
- **Authentication**: JWT Tokens
- **AI Integration**: OpenAI-compatible agent
- **Database**: PostgreSQL (with Neon as cloud option)

## API Endpoints

### Authentication
- `POST /api/auth/signup` - Create new user
- `POST /api/auth/signin` - Login user
- `POST /api/auth/signout` - Logout user

### Todo Management
- `GET /api/todos` - Get user's todos
- `POST /api/todos` - Create new todo
- `PUT /api/todos/{id}` - Update todo
- `PATCH /api/todos/{id}/complete` - Toggle completion
- `DELETE /api/todos/{id}` - Delete todo

### AI Assistant
- `POST /api/chat` - Chat with AI assistant

## Setup and Installation

### Prerequisites
- Python 3.9+
- PostgreSQL (or Neon for cloud database)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ayeshaaaqil/backend-phase-2-and-3.git
   cd backend-phase-2-and-3
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory with the following:
   ```env
   SECRET_KEY=your-super-secret-key-change-in-production
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   NEON_DATABASE_URL=your-neon-database-url
   OPENAI_API_KEY=your-openai-api-key-if-using
   ```

5. **Initialize the database**
   ```bash
   python initialize_db.py
   ```

6. **Run the application**
   ```bash
   cd src
   python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

## Environment Variables

- `SECRET_KEY`: Secret key for JWT tokens (use a strong random key)
- `ALGORITHM`: Algorithm for JWT (default: HS256)
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Token expiration time (default: 30)
- `NEON_DATABASE_URL`: PostgreSQL connection string for Neon database
- `OPENAI_API_KEY`: OpenAI API key if using OpenAI features

## Usage

Once the server is running, you can access the API at `http://localhost:8000`.

The AI assistant can process natural language commands like:
- "Add 'buy groceries' to my todos"
- "Show me my todos"
- "Update 'buy groceries' to 'buy groceries and milk'"
- "Mark 'buy groceries' as complete"
- "Delete 'buy groceries'"

## Deployment

### Deploy to Hugging Face Spaces

This backend is designed to be deployed on Hugging Face Spaces. Follow the instructions in the `DEPLOYMENT_GUIDE.md` file.

### Deploy to Other Platforms

For other deployment options, you can containerize the application using the provided Dockerfile.

## Project Structure

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
├── requirements.txt     # Python dependencies
├── Dockerfile          # Docker configuration
├── initialize_db.py    # Database initialization script
└── README.md
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any issues, please open an issue in the GitHub repository.