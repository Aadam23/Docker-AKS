<h1>Flask App on Docker and Azure Kubernetes Service (AKS)</h1>
<br />

<h2>Project Overview</h2>
<p>This project demonstrates how to containerize a Python Flask application using Docker and deploy it to Azure Kubernetes Service (AKS). The application is exposed using a LoadBalancer, making it accessible via an external IP.</p>
<br />

<h2>Diagram:</h2>
<p align="center"><img width="1440" alt="Screenshot 2024-11-20 at 3 01 57 PM" src="https://github.com/user-attachments/assets/fff79c8e-6df4-4904-b3d6-a2337ef8f32a"></p>
<br>

<h2>Features</h2>

- **Dockerized Flask Application**: A lightweight Python Flask app.
- **Azure Kubernetes Service (AKS)**: Deployed and managed using Kubernetes.
- **Azure Container Registry (ACR)**: Securely stores the Docker image.


<h2>Tools & Technologies Used</h2>

- **Python**: The core language used to develop the Flask web application.
- **Flask**: A lightweight Python web framework used to create the web application.
- **Docker**: Used to containerize the Flask application, making it portable and scalable.
- **Azure Container Registry (ACR)**: Securely stores the Docker image and makes it accessible to the Azure Kubernetes Service.
- **Azure Kubernetes Service (AKS)**: A managed Kubernetes service to deploy, scale, and manage containerized applications in the cloud.
- **Kubernetes LoadBalancer Service**: Exposes the application to the internet using a public IP address.
- **Azure CLI**: Command-line interface to manage Azure resources, including ACR and AKS.
- **kubectl**: Command-line tool to interact with Kubernetes for managing the deployment and service.
- **VS Code**: Used for writing and editing the application and Kubernetes manifests (deployment.yaml and service.yaml)
- **Git**: For version control and pushing the project to GitHub.
- **Linux/amd64**: The target platform for the Docker image to ensure compatibility with AKS nodes.
- **Ubuntu 22.04 LTS**: The operating system running on the AKS nodes.
- **kubectl logs and kubectl describe**: Used for debugging Kubernetes pods and services.
<br />


<h2>Architecture</h2>

1. Flask app containerized with Docker.
2. Docker image pushed to Azure Container Registry (ACR).
3. AKS cluster pulls the image and deploys the app.
4. App exposed via LoadBalancer for external access.
<br />


<h2>Steps</h2>

Setup Instructions:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>

2. **Clone the Repository**:
   ```bash
   docker buildx build --platform linux/amd64 -t <your-acr-name>.azurecr.io/flask-app:latest .
   docker push <your-acr-name>.azurecr.io/flask-app:latest
   
3. **Clone the Repository**:
   ```bash
   az aks create --resource-group <resource-group-name> --name <aks-cluster-name> --node-count 1 --enable-addons monitoring --generate-ssh-keys
   az aks update -n <aks-cluster-name> -g <resource-group-name> --attach-acr <your-acr-name>

4. **Clone the Repository**:
   ```bash
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml

5. **Clone the Repository**:
   ```bash
   kubectl get services
Use the EXTERNAL-IP to access the app in a browser.
