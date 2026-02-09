# Carbi Play (Railway-ready)

This repo contains:
- `backend/` FastAPI API (Docker) + Postgres-ready (Railway Postgres)
- `admin/` React-Admin panel (Docker) to manage channels, sources, devices, etc.

## Quick deploy on Railway (single place = one Railway Project)
1) Create a new Railway Project and connect this repository.
2) Add **Postgres** plugin in the same project.
3) Create a **Service** from this repo for the backend:
   - Root directory: `backend`
4) Create another **Service** from this repo for the admin:
   - Root directory: `admin`
5) Set environment variables (backend service):
   - DATABASE_URL = (from Railway Postgres)
   - JWT_SECRET = a strong random string
   - CORS_ORIGINS = https://<your-admin-domain>,https://<your-user-web-domain> (optional for Android)
   - ADMIN_EMAIL = admin@carbi.play
   - ADMIN_PASSWORD = admin123 (change)
6) Set environment variables (admin service):
   - VITE_API_URL = https://<your-backend-domain>

## Local dev
`docker compose up --build` (see docker-compose.yml)

Backend:
- https://<backend>/docs

Admin:
- https://<admin>/

Notes:
- The backend listens on `$PORT` (Railway requirement).
- Device gate endpoints:
  - POST /device/register
  - GET /device/status
All other endpoints are protected by device approval + auth where applicable.
