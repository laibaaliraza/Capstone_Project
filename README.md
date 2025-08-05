# 3-Day DevOps Capstone

## Phases
1. FastAPI App + PostgreSQL + Migration Scripts
2. Backup Container + Cron + GitOps Versioning
3. CI/CD with GitHub Actions + NGINX Web Interface

## Run Locally
```bash
docker-compose up --build
curl http://localhost:8000/tasks
curl http://localhost:8080/backups/
