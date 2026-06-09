# Flask DevOps App

A simple Python Flask web application deployed using modern DevOps tools.

## Tech Stack
- **Python Flask** - Web application
- **Docker** - Containerization
- **Kubernetes** - Container orchestration
- **Helm** - Kubernetes package manager

## Project Structure

devops-app-flask/
├── app.py              # Flask application
├── Dockerfile          # Docker image definition
├── requirements.txt    # Python dependencies
├── deployment.yaml     # Kubernetes Deployment
├── service.yaml        # Kubernetes Service
└── flask-chart/        # Helm chart

## How to Run

### Using Docker
```bash
docker pull pavanreddy6/devops-app-flask:v1
docker run -p 5000:5000 pavanreddy6/devops-app-flask:v1
```

### Using Kubernetes
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### Using Helm
```bash
helm install flask-release ./flask-chart
```