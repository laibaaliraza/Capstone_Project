# DevOps Capstone Project (FastAPI + PostgreSQL + Docker + CI/CD) 

This DevOps Capstone Project use:

- FastAPI
- PostgreSQL
- Docker Compose
- cron
- NGINX
- GitHub Actions



# Features

- Modular FastAPI application
- PostgreSQL database with volume persistence
- Docker Compose orchestration
- Cron-based automated database backups
- NGINX reverse proxy for routing
- GitHub Actions CI/CD


# Project Structure

Capstone_Project/
app/
    ─ main.py                # FastAPI entry point
    ─ routes/                # API routes
        -team_capstone.py    
    ─ schemas/               # Pydantic models
        -team_capstone.py 
    ─ models/                # SQLAlchemy models
        -team_capstone.py 
backup/
    -Dockerfile
scripts/
    -search_backup.sh
    -cronjob
nginx/
    -nginx.conf           # NGINX config

.github/
    ─ workflows/
    ─ ci.yml           # GitHub Actions workflow

─ Dockerfile                 # FastAPI image build config
─ docker-compose.yml         # Docker Compose definition
─ requirements.txt           # Python dependencies
─ README.md                  # Project documentation


# How to Run the Project

# OS should have:

- Docker
- Docker Compose
- Git


# Quick Start

```bash
# Clone the repository
git clone https://github.com/laibaaliraza/team_capstone
cd team_capstone

# Build and start containers
docker compose up --build -d
```

- Visit the API at: [http://localhost:8000](http://localhost:8000)
- View Swagger docs: [http://localhost:8000/docs](http://localhost:8000/docs)


# Example API Route

GET /team_capstone

- Returns a list of team members for the project.

# Database Backups

Backups are handled by a cron job inside the `backup` container.

# Automatic Backups

- Backup script: `scripts/search_backup.sh`
- Cron schedule defined in: `sripts/cronjob`
- Output stored in: `backups/`

# Manual Backup (Optional)

docker compose exec backup bash /scripts/search_backup.sh


# NGINX Reverse Proxy

- Configured in `nginx/nginx.conf`
- Proxies HTTP requests to the FastAPI app
- Accessible via `http://localhost/` if mapped to port 80

---

# GitHub Actions CI/CD

Automatically triggered on `git push`.

# Workflow Includes:

- Code checkout
- Docker image build
- (Optional) Push to Docker Hub
- (Optional) SSH deploy to cloud

# Config:

.github/workflows/ci.yml


# Docker Hub Integration (Optional)

To push image to Docker Hub:

docker tag fastapi_app yourdockerhub/fastapi_app
docker push yourdockerhub/fastapi_app


Set Docker credentials as GitHub secrets.


# Deployment Checklist

- FastAPI routes working
- PostgreSQL DB connected
- Docker Compose running all services
- Backups scheduled and working
- NGINX routing correctly
- CI/CD configured in GitHub Actions

# Author

Laiba 
-> FastAPI • Docker • CI/CD_

