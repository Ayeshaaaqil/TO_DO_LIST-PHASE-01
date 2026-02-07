# Cleanup Script: Remove All Deployed Resources

This script removes all resources deployed as part of the Cloud Native Todo Chatbot Kubernetes deployment.

## Cleanup Commands

### 1. Uninstall Helm Release
```bash
helm uninstall todo-chatbot
```

### 2. Remove Docker Images (Optional)
```bash
# Remove the images from Minikube's Docker environment
docker rmi ayesha/todo-frontend:v1
docker rmi ayesha/todo-backend:v1
```

### 3. Delete Minikube Cluster
```bash
minikube delete
```

### 4. Reset Kubernetes Context (Optional)
```bash
kubectl config delete-context minikube
kubectl config delete-cluster minikube
kubectl config unset users.minikube
```

## Complete Cleanup Script

Here's a complete script that performs all cleanup operations:

```bash
#!/bin/bash

echo "Starting cleanup of Cloud Native Todo Chatbot deployment..."

# Uninstall Helm release
echo "Uninstalling Helm release..."
helm uninstall todo-chatbot 2>/dev/null || echo "Helm release not found or already uninstalled"

# Remove Docker images
echo "Removing Docker images..."
docker rmi ayesha/todo-frontend:v1 2>/dev/null || echo "Frontend image not found"
docker rmi ayesha/todo-backend:v1 2>/dev/null || echo "Backend image not found"

# Delete Minikube cluster
echo "Deleting Minikube cluster..."
minikube delete

# Reset kubectl context
echo "Resetting kubectl context..."
kubectl config delete-context minikube 2>/dev/null || echo "Minikube context not found"
kubectl config delete-cluster minikube 2>/dev/null || echo "Minikube cluster not found"
kubectl config unset users.minikube 2>/dev/null || echo "Minikube user not found"

echo "Cleanup completed!"
```

For Windows users, the equivalent PowerShell script would be:

```powershell
Write-Host "Starting cleanup of Cloud Native Todo Chatbot deployment..."

# Uninstall Helm release
Write-Host "Uninstalling Helm release..."
helm uninstall todo-chatbot 2>$null || Write-Host "Helm release not found or already uninstalled"

# Remove Docker images
Write-Host "Removing Docker images..."
docker rmi ayesha/todo-frontend:v1 2>$null || Write-Host "Frontend image not found"
docker rmi ayesha/todo-backend:v1 2>$null || Write-Host "Backend image not found"

# Delete Minikube cluster
Write-Host "Deleting Minikube cluster..."
minikube delete

# Reset kubectl context
Write-Host "Resetting kubectl context..."
kubectl config delete-context minikube 2>$null || Write-Host "Minikube context not found"
kubectl config delete-cluster minikube 2>$null || Write-Host "Minikube cluster not found"
kubectl config unset users.minikube 2>$null || Write-Host "Minikube user not found"

Write-Host "Cleanup completed!"
```

## Verification

After running the cleanup script, verify that all resources have been removed:

```bash
# Verify no pods are running
kubectl get pods

# Verify no services exist
kubectl get services

# Verify no deployments exist
kubectl get deployments

# Verify Helm releases are gone
helm list
```

All commands should return empty results or indicate that no resources were found.