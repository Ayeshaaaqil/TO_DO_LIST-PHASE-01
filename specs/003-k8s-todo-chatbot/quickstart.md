# Quickstart Guide: Kubernetes Deployment for Cloud Native Todo Chatbot

**Feature**: 3-k8s-todo-chatbot
**Created**: 2026-01-30

## Prerequisites

1. Docker Desktop (≥4.38) with Gordon AI enabled
2. Minikube
3. Helm 3+
4. kubectl
5. kubectl-ai plugin
6. kagent

## Setup Steps

### 1. Enable Docker AI (Gordon)
1. Open Docker Desktop
2. Go to Settings → Features in development
3. Enable "Docker AI Agent (Gordon)"
4. Restart Docker Desktop if prompted

### 2. Start Minikube
```bash
minikube start --driver=docker --memory=4096 --cpus=2
```

### 3. Build and Load Images
```bash
# Set Docker environment to Minikube
eval $(minikube docker-env)

# Build frontend image
docker build -f ./frontend/Dockerfile -t ayesha/todo-frontend:v1 ./frontend

# Build backend image
docker build -f ./backend/Dockerfile -t ayesha/todo-backend:v1 ./backend
```

### 4. Install kubectl-ai
```bash
# For Linux/macOS
curl -fsSL https://raw.githubusercontent.com/GoogleCloudPlatform/kubectl-ai/main/install.sh | bash

# For Windows (using PowerShell)
curl -fsSL https://raw.githubusercontent.com/GoogleCloudPlatform/kubectl-ai/main/install.ps1 | powershell -command -
```

### 5. Deploy Using Helm
```bash
# Navigate to helm charts directory
cd helm/todo-chatbot

# Install the chart
helm install todo-chatbot .
```

### 6. Access the Application
```bash
# Get the frontend service URL
minikube service todo-frontend --url
```

## AI-Assisted Commands

### Using kubectl-ai
```bash
# Scale backend to 3 replicas
kubectl-ai "scale the backend deployment to 3 replicas"

# Check why pods are failing
kubectl-ai "why are the backend pods in CrashLoopBackOff?"

# Create a new service
kubectl-ai "create a service for the frontend application"
```

### Using kagent
```bash
# Analyze cluster health
kagent "analyze cluster health"

# Optimize resource allocation
kagent "optimize resource allocation for todo pods"
```

## Troubleshooting

### Common Issues
1. **Images not found**: Ensure you've run `eval $(minikube docker-env)` before building images
2. **Service not accessible**: Check if Minikube is running with `minikube status`
3. **Insufficient resources**: Increase Minikube resources with `minikube delete` followed by `minikube start --memory=6g --cpus=4`

### AI Troubleshooting
```bash
# Use kubectl-ai to diagnose issues
kubectl-ai "show me the logs for the backend pods"

# Use kagent for deeper analysis
kagent "debug why the frontend pods are not starting"
```