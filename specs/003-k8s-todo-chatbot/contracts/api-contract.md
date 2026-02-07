# API Contract: Todo Chatbot Backend API

**Feature**: 3-k8s-todo-chatbot
**Created**: 2026-01-30
**Base URL**: http://todo-backend:5000 (internal) or http://localhost:5000 (external)

## Todo Management Endpoints

### GET /todos
**Description**: Retrieve all todo items
**Authentication**: Required
**Response**:
- 200 OK: Array of todo items
```
[
  {
    "id": "uuid-string",
    "title": "Todo title",
    "description": "Todo description",
    "completed": false,
    "createdAt": "2023-01-01T00:00:00Z",
    "updatedAt": "2023-01-01T00:00:00Z"
  }
]
```

### POST /todos
**Description**: Create a new todo item
**Authentication**: Required
**Request Body**:
```
{
  "title": "Todo title",
  "description": "Todo description"
}
```
**Response**:
- 201 Created: Created todo item
```
{
  "id": "uuid-string",
  "title": "Todo title",
  "description": "Todo description",
  "completed": false,
  "createdAt": "2023-01-01T00:00:00Z",
  "updatedAt": "2023-01-01T00:00:00Z"
}
```

### PUT /todos/{id}
**Description**: Update an existing todo item
**Authentication**: Required
**Parameters**:
- id (path): UUID of the todo item
**Request Body**:
```
{
  "title": "Updated title",
  "description": "Updated description",
  "completed": true
}
```
**Response**:
- 200 OK: Updated todo item
```
{
  "id": "uuid-string",
  "title": "Updated title",
  "description": "Updated description",
  "completed": true,
  "createdAt": "2023-01-01T00:00:00Z",
  "updatedAt": "2023-01-02T00:00:00Z"
}
```

### DELETE /todos/{id}
**Description**: Delete a todo item
**Authentication**: Required
**Parameters**:
- id (path): UUID of the todo item
**Response**:
- 204 No Content: Successfully deleted

## Chat Endpoints

### POST /chat
**Description**: Send a message to the chatbot
**Authentication**: Required
**Request Body**:
```
{
  "message": "User message",
  "conversationId": "existing-conversation-id (optional)"
}
```
**Response**:
- 200 OK: Chat response
```
{
  "reply": "Chatbot response",
  "conversationId": "conversation-id"
}
```

## Health Check Endpoint

### GET /health
**Description**: Check the health status of the backend service
**Authentication**: Not required
**Response**:
- 200 OK: Service is healthy
```
{
  "status": "healthy",
  "timestamp": "2023-01-01T00:00:00Z"
}
```