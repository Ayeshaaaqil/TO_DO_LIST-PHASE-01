# Research Summary: Kubernetes Deployment for Cloud Native Todo Chatbot

**Feature**: 3-k8s-todo-chatbot
**Created**: 2026-01-30

## Decision 1: Docker AI (Gordon) Capabilities and Setup

**Rationale**: Docker AI (Gordon) is Docker's AI-powered assistant that helps with containerization tasks. It's available in Docker Desktop 4.38+ and can be accessed via the "Ask Gordon" feature in the Docker Desktop UI or via CLI commands like `docker ai "question"`.

**Alternatives considered**:
- Manual Dockerfile creation: More time-consuming and error-prone
- Third-party Dockerfile generators: Less integrated and potentially less reliable

## Decision 2: kubectl-ai Installation Process for Windows

**Rationale**: kubectl-ai can be installed on Windows by downloading the binary from the GitHub releases page and adding it to the PATH. The installation process involves:
1. Download the appropriate binary for Windows
2. Place it in a directory in the PATH
3. Verify installation with `kubectl ai version`

**Alternatives considered**:
- Using curl | bash (not available on Windows by default): Would require additional tools like Git Bash or WSL2
- Building from source: More complex and time-consuming

## Decision 3: kagent Configuration for Minikube

**Rationale**: kagent is installed as CRDs and a controller in the cluster. For Minikube, it can be installed using kubectl apply commands. It may require a local LLM (like Ollama) or API key for operation. The installation process involves:
1. Apply kagent CRDs and controller to the cluster
2. Configure with LLM provider (local Ollama or cloud API)
3. Verify installation with kagent commands

**Alternatives considered**:
- Using standard kubectl without AI assistance: Loses the AI benefits
- Using cloud-based kagent: May incur costs and require internet connectivity

## Decision 4: Image Naming Convention

**Rationale**: Using the naming convention `ayesha/todo-frontend:v1` and `ayesha/todo-backend:v1` as specified in the requirements. These names are clear, descriptive, and follow common Docker image naming conventions.

**Alternatives considered**:
- Using generic names like `frontend:latest`: Less descriptive and harder to manage versions
- Using complex naming schemes: Overly complicated for a local deployment

## Decision 5: Helm Chart Structure

**Rationale**: Creating a unified Helm chart that manages both frontend and backend deployments. This approach simplifies deployment and management while keeping related services together.

**Alternatives considered**:
- Separate charts for frontend and backend: More complex to manage and deploy together
- Single deployment with both containers: Doesn't follow microservices best practices

## Decision 6: Service Communication Pattern

**Rationale**: Using Kubernetes internal DNS for service-to-service communication. The frontend will connect to the backend using the service name (e.g., `http://todo-backend:5000`).

**Alternatives considered**:
- Using environment variables for backend URL: Requires more configuration
- Using a service mesh: Too complex for a basic local deployment