# Cloud Native Todo Chatbot - Kubernetes Deployment

This project deploys a cloud-native Todo Chatbot application to a local Kubernetes cluster using Minikube, with AI-assisted tooling for containerization, deployment, and operations.

## Prerequisites

Before starting, ensure you have the following tools installed:

1. **Docker Desktop** (≥4.38) with Gordon AI enabled
   - Download from: https://www.docker.com/products/docker-desktop/
   - Enable Gordon AI in Settings → Features in development → Enable Docker AI

2. **Minikube** (latest version)
   - For Windows: `choco install minikube` (requires Chocolatey)
   - Or download from: https://github.com/kubernetes/minikube/releases/latest

3. **Helm 3+**
   - For Windows: `choco install kubernetes-helm`

4. **kubectl**
   - For Windows: `choco install kubernetes-cli`

5. **kubectl-ai plugin**
   - Download from: https://github.com/GoogleCloudPlatform/kubectl-ai/releases
   - Place the binary in your PATH

6. **kagent**
   - Install with: `kubectl apply -f https://github.com/kagent-dev/kagent/releases/latest/download/kagent.yaml`

## Setup Instructions

### 1. Enable Gordon AI in Docker Desktop
1. Open Docker Desktop
2. Go to Settings → Features in development
3. Enable "Docker AI Agent (Gordon)"
4. Restart Docker Desktop if prompted

### 2. Start Minikube
```bash
minikube start --driver=docker --memory=4096 --cpus=2
```

### 3. Build Docker Images
First, set Docker environment to Minikube:
```bash
# On Windows with PowerShell
& minikube docker-env | Invoke-Expression

# On Windows with Command Prompt
FOR /f "tokens=*" %i IN ('minikube docker-env') DO @%i
```

Then build the images:
```bash
# Build frontend image
docker build -f ./frontend/Dockerfile -t ayesha/todo-frontend:v1 ./frontend

# Build backend image
docker build -f ./backend/Dockerfile -t ayesha/todo-backend:v1 ./backend
```

## Deployment Instructions

### 1. Deploy Using Helm
Navigate to the Helm charts directory and install:
```bash
cd helm/todo-chatbot
helm install todo-chatbot .
```

### 2. Access the Application
Get the frontend service URL:
```bash
minikube service todo-chatbot-frontend --url
```

Or use port forwarding:
```bash
kubectl port-forward svc/todo-chatbot-frontend 3000:3000
```

## AI-Assisted Operations

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
1. **Images not found**: Ensure you've run `minikube docker-env` before building images
2. **Service not accessible**: Check if Minikube is running with `minikube status`
3. **Insufficient resources**: Increase Minikube resources with `minikube delete` followed by `minikube start --memory=6g --cpus=4`

### AI Troubleshooting
```bash
# Use kubectl-ai to diagnose issues
kubectl-ai "show me the logs for the backend pods"

# Use kagent for deeper analysis
kagent "debug why the frontend pods are not starting"
```

## Cleanup

To remove all deployed resources:
```bash
helm uninstall todo-chatbot
minikube delete
```

## Regional Considerations

If you're experiencing slow downloads or blocked access (common in regions like Pakistan):
- Consider using a VPN to access Docker Hub or GitHub
- Use regional mirrors if available
- Download binaries manually if needed

## Architecture

The deployment consists of:
- Frontend: React/Vite application running on port 3000
- Backend: Node.js/Express API running on port 5000
- Communication: Internal Kubernetes DNS (frontend connects to backend via service name)
- Persistence: SQLite database (can be upgraded to PostgreSQL in production)

## Spec-Driven Development

This deployment follows a spec-driven development approach using the blueprint.md file. The structured specification allows AI tools to generate and manage Kubernetes resources effectively.