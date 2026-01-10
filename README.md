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
- Fully Dockerized & Cloud Deployed

---

## 📦 Architecture

```text
User → Browser
      ↓
   Nginx (Reverse Proxy)
      ↓
   Gunicorn (Django App)
      ↓
   MongoDB Atlas (Cloud Database)

Code Execution Flow:
User Code → Language-specific Docker Container → Output → Django → User
