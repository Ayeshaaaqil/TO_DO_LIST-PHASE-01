# Phase II: Full-Stack Web Application

This directory (C:\Users\Dell\Desktop\phase2) represents Phase II of the "Evolution of Todo" project - a full-stack web application with user authentication and todo management features.

## Features

- User authentication (signup/signin)
- Todo management (create, read, update, delete)
- Mark todos as complete/incomplete
- User-specific data isolation
- Responsive UI for desktop and mobile
- API endpoints for all operations

## Tech Stack

### Backend
- Python 3.13+
- FastAPI
- SQLModel
- Neon PostgreSQL
- JWT for authentication

### Frontend
- Next.js 14+
- TypeScript
- Tailwind CSS

## Subdirectories
- `backend/` - Backend API implementation
- `frontend/` - Frontend application
- `src/` - Shared source code
- `specs/` - Project specifications
- `history/` - Project history and prompts

## API Endpoints

### Authentication
- `POST /api/auth/signup` - Create a new user
- `POST /api/auth/signin` - Authenticate a user
- `POST /api/auth/signout` - Sign out a user

### Todos
- `GET /api/todos` - Get all todos for the authenticated user
- `POST /api/todos` - Create a new todo
- `GET /api/todos/{id}` - Get a specific todo
- `PUT /api/todos/{id}` - Update a specific todo
- `PATCH /api/todos/{id}/complete` - Toggle todo completion status
- `DELETE /api/todos/{id}` - Delete a specific todo