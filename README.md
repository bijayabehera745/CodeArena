# CodeArena – Online Coding Platform (Django + Docker + AWS)

## 🚀 Overview

CodeArena is a full-stack online coding platform inspired by LeetCode and CodeChef.  
It allows users to register, log in, solve coding problems, submit code in multiple languages, and view leaderboards.  
The platform is fully containerized using Docker and deployed on AWS with MongoDB Atlas as the backend database.

---

## 🛠️ Tech Stack

### Backend
- Python
- Django
- Gunicorn

### Frontend
- Django Templates
- Bootstrap 5

### Database
- MongoDB Atlas (via Djongo)

### DevOps & Deployment
- Docker
- Docker Compose
- AWS EC2 (Ubuntu)
- Environment-based configuration (.env)

### Code Execution Engine
- Isolated Docker containers for:
  - C++
  - Java
  - Python

---

## ✨ Features

- User Authentication (Login / Register / Logout)
- Problem Listing & Detailed Problem View
- Code Submission System
- Multi-language Code Execution (C++, Java, Python)
- Automatic Output Validation
- Leaderboard System
- Secure Environment Variable Handling
- Fully Dockerized & Cloud Deployed on AWS

---

## 📦 Architecture

```text
User → Browser
      ↓
   Gunicorn (Django App running inside Docker)
      ↓
   MongoDB Atlas (Cloud Database)

Code Execution Flow:
User Code → Language-specific Docker Container → Output → Django → User
```
---

## ⚙️ Local Setup
```
git clone https://github.com/yourusername/codearena.git
cd codearena
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver

```
---

## 🐳 Docker Setup
```
docker-compose up -d --build

```

---

## 🌍 Live Deployment

Deployed on AWS EC2 using Docker & Docker Compose
Application served using Gunicorn inside Docker
Database hosted on MongoDB Atlas

## 🧠 Learning Outcomes

Hands-on experience with Docker & Docker Compose

Cloud deployment using AWS EC2

Secure configuration using environment variables

Real-world backend architecture design

Debugging production-level issues (Gunicorn, MongoDB, Docker, AWS networking)
