<div align="center">

# 🍇 Wine Quality Prediction API

### Production-ready FastAPI application for predicting wine quality using a trained Random Forest model

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![MLflow](https://img.shields.io/badge/MLflow-Integrated-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)](https://mlflow.org/)
[![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com/)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/features/actions)

</div>

---

## 📖 Overview

A robust, containerized machine learning API that predicts **wine quality scores** from physicochemical properties using a trained **Random Forest** model. Built with modern MLOps practices — from experiment tracking to automated deployment.

---

## ✨ Features

| Feature | Description |
|---|---|
| ⚡ **FastAPI Framework** | Modern, fast, asynchronous web framework for building APIs |
| 📊 **MLflow Integration** | Standardized ML model management and experiment tracking |
| ✅ **Pydantic Validation** | Automatic request validation for reliable inference |
| 🐳 **Dockerized** | Fully containerized for easy deployment and scalability |
| 🔄 **CI/CD Pipeline** | Automated build, push, and deployment via GitHub Actions |
| 💓 **Health Checks** | Comprehensive `/health` endpoint for uptime monitoring |
| 🔐 **Environment Variables** | Securely managed via `.env` files |
| 📝 **Structured Logging** | Request and error logging for observability |

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology |
|:---:|:---:|
| **Web Framework** | FastAPI |
| **ML Model** | Scikit-learn (Random Forest) |
| **Experiment Tracking** | MLflow |
| **Containerization** | Docker |
| **Deployment** | Render |
| **CI/CD** | GitHub Actions |
| **Registry** | GitHub Container Registry (GHCR) |

</div>

---

## 📋 Prerequisites

- 🐍 Python 3.7+
- 🐳 Docker Desktop
- 🐙 A GitHub repository with CI/CD configured

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run locally

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 4️⃣ Or run with Docker

```bash
docker build -t wine-quality-api .
docker run -p 8000:8000 wine-quality-api
```

The API will be available at **`http://localhost:8000`** 🎉

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|:---:|---|---|
| `GET` | `/health` | Returns API health status |
| `POST` | `/predict` | Predicts wine quality from input features |
| `GET` | `/docs` | Interactive Swagger UI documentation |

---

## 🔄 CI/CD Pipeline

<div align="center">

```
   📝 Push to main
        │
        ▼
   🧪 Build & Test
        │
        ▼
   🐳 Build Docker Image
        │
        ▼
   📦 Push to GHCR
        │
        ▼
   🚀 Deploy to Render
```

</div>

Every push to `main` automatically builds a fresh Docker image, pushes it to **GitHub Container Registry**, and triggers a **zero-touch deployment** to Render.

---

## 📂 Project Structure

```
.
├── app/
│   ├── main.py            # FastAPI application entrypoint
│   └── ...
├── .github/
│   └── workflows/
│       └── ci-cd.yml       # GitHub Actions pipeline
├── Dockerfile
├── .dockerignore
├── requirements.txt
└── README.md
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open a pull request.

---

<div align="center">

Made with ❤️ and 🍷 

</div>
