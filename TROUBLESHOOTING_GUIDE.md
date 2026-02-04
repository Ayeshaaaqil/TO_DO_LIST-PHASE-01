# Troubleshooting Guide: Kubernetes Deployment for Cloud Native Todo Chatbot

## Common Issues and Solutions

### 1. Docker Images Not Found in Minikube

**Problem**: Pods fail to start with "ImagePullBackOff" or "ErrImagePull" errors.

**Solution**:
1. Ensure you've set the Docker environment to Minikube:
   ```bash
   # On Windows with PowerShell
   & minikube docker-env | Invoke-Expression
   
   # On Windows with Command Prompt
   FOR /f "tokens=*" %i IN ('minikube docker-env') DO @%i
   ```
   
2. Rebuild the images after setting the environment:
   ```bash
   docker build -f ./frontend/Dockerfile -t ayesha/todo-frontend:v1 ./frontend
   docker build -f ./backend/Dockerfile -t ayesha/todo-backend:v1 ./backend
   ```

### 2. Minikube Not Starting

**Problem**: Minikube fails to start with driver or resource errors.

**Solution**:
1. Check available resources:
   ```bash
   minikube start --driver=docker --memory=4096 --cpus=2
   ```
   
2. If resources are insufficient, increase them:
   ```bash
   minikube delete
   minikube start --driver=docker --memory=6144 --cpus=4
   ```

### 3. Services Not Accessible

**Problem**: Cannot access the frontend via browser.

**Solution**:
1. Check if services are running:
   ```bash
   kubectl get svc
   ```
   
2. Get the service URL:
   ```bash
   minikube service todo-chatbot-frontend --url
   ```
   
3. Or use port forwarding:
   ```bash
   kubectl port-forward svc/todo-chatbot-frontend 3000:3000
   ```

### 4. Frontend Cannot Connect to Backend

**Problem**: Frontend shows errors when trying to access backend APIs.

**Solution**:
1. Verify backend service is running:
   ```bash
   kubectl get svc todo-chatbot-backend
   ```
   
2. Check if backend pods are healthy:
   ```bash
   kubectl get pods -l app=backend
   ```
   
3. Verify the connection URL in frontend environment variables:
   ```bash
   kubectl describe deployment todo-chatbot-frontend
   ```

## AI-Assisted Troubleshooting

### Using kubectl-ai for Diagnostics

1. **Check pod status and logs**:
   ```bash
   kubectl-ai "show me the status of all pods in the default namespace"
   kubectl-ai "show me the logs for the backend pods"
   ```

2. **Diagnose specific issues**:
   ```bash
   kubectl-ai "why are the backend pods in CrashLoopBackOff?"
   kubectl-ai "check if there are any resource constraints affecting the deployments"
   ```

3. **Scale resources**:
   ```bash
   kubectl-ai "scale the backend deployment to 2 replicas"
   kubectl-ai "increase memory limits for the frontend deployment to 256Mi"
   ```

### Using kagent for Advanced Analysis

1. **Analyze cluster health**:
   ```bash
   kagent "analyze cluster health"
   ```

2. **Optimize resource allocation**:
   ```bash
   kagent "optimize resource allocation for todo pods"
   ```

3. **Debug complex issues**:
   ```bash
   kagent "debug why the frontend pods are not starting"
   kagent "analyze resource utilization in the cluster"
   ```

## Network and Region-Specific Issues

### Slow Downloads or Blocked Access

If you're experiencing slow downloads or blocked access (common in regions like Pakistan):

1. **Use a VPN** to access Docker Hub or GitHub
2. **Try regional mirrors** if available
3. **Download binaries manually** if needed

### Docker Hub Rate Limits

If encountering Docker Hub rate limits:

1. **Create a Docker Hub account** and authenticate:
   ```bash
   docker login
   ```
   
2. **Use authenticated pulls** in your deployments

## Verification Commands

### Check Overall Status
```bash
kubectl get all
helm list
minikube status
```

### Check Specific Components
```bash
# Check deployments
kubectl get deployments

# Check services
kubectl get services

# Check pods
kubectl get pods

# Check if all pods are running
kubectl get pods -o wide
```

### Check Application Logs
```bash
# Frontend logs
kubectl logs -l app=frontend

# Backend logs
kubectl logs -l app=backend
```

## Cleanup and Reset

### If Things Go Wrong
```bash
# Uninstall the Helm release
helm uninstall todo-chatbot

# Delete all resources in the namespace
kubectl delete all --all

# Restart Minikube
minikube delete
minikube start --driver=docker --memory=4096 --cpus=2
```

### Fresh Start Procedure
1. Uninstall the Helm release
2. Delete Minikube cluster
3. Rebuild Docker images
4. Restart Minikube
5. Reinstall Helm chart

## Useful Commands

### General Kubernetes Commands
```bash
# Get detailed info about a resource
kubectl describe <resource-type> <resource-name>

# Execute commands inside a pod
kubectl exec -it <pod-name> -- /bin/sh

# Port forward for local access
kubectl port-forward <pod-name> <local-port>:<container-port>
```

### Helm Commands
```bash
# Check release status
helm status todo-chatbot

# Upgrade the release
helm upgrade todo-chatbot ./path-to-chart

# Rollback to previous version
helm rollback todo-chatbot
```

### Minikube Commands
```bash
# Get service URLs
minikube service <service-name> --url

# Open dashboard
minikube dashboard

# SSH into the cluster
minikube ssh
```