# Data Model: Kubernetes Deployment for Cloud Native Todo Chatbot

**Feature**: 3-k8s-todo-chatbot
**Created**: 2026-01-30

## Kubernetes Resources

### Frontend Deployment
- **Kind**: Deployment
- **Name**: todo-frontend
- **Replicas**: 1 (scalable)
- **Container Image**: ayesha/todo-frontend:v1
- **Ports**: 3000 (HTTP)
- **Environment Variables**:
  - REACT_APP_API_URL: URL of the backend service

### Frontend Service
- **Kind**: Service
- **Name**: todo-frontend
- **Type**: ClusterIP or LoadBalancer
- **Port**: 3000
- **Target Port**: 3000
- **Selector**: app=frontend

### Backend Deployment
- **Kind**: Deployment
- **Name**: todo-backend
- **Replicas**: 1 (scalable)
- **Container Image**: ayesha/todo-backend:v1
- **Ports**: 5000 (HTTP)
- **Environment Variables**:
  - DATABASE_URL: Connection string for the database
  - FRONTEND_URL: URL of the frontend service

### Backend Service
- **Kind**: Service
- **Name**: todo-backend
- **Type**: ClusterIP
- **Port**: 5000
- **Target Port**: 5000
- **Selector**: app=backend

## Application Data Models (Existing)

### Todo Entity
- **id**: Unique identifier (string/UUID)
- **title**: Title of the todo item (string)
- **description**: Detailed description (string, optional)
- **completed**: Status of completion (boolean)
- **createdAt**: Timestamp of creation (datetime)
- **updatedAt**: Timestamp of last update (datetime)

### Chat Message Entity
- **id**: Unique identifier (string/UUID)
- **sender**: Who sent the message (string)
- **message**: Content of the message (string)
- **timestamp**: When the message was sent (datetime)
- **conversationId**: ID of the conversation thread (string)