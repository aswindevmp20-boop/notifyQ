# notifyQ


alembic:- 

alembic init alembic

FastAPI running:-

python3 -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

Install dependencies:-

pip install -r requirements.txt




⚙️ ✅ Full Startup Workflow (Before Running APIs)

This is your go-to checklist every time you open your Codespace or restart your system.

🧩 Step 1 — Start Docker Services

You need PostgreSQL and Redis running for your app to work.
Check first:

docker ps


If you don’t see postgres and redis containers running, start them:

docker compose up -d


✅ This will start:

notifyiq_db (PostgreSQL)

notifyiq_redis (Redis)

(optionally) your Celery worker if defined in compose file

⚙️ Step 2 — Start Celery Worker

Celery handles all background tasks (/notify → send email).

If the worker is not running inside Docker, start it manually in a new terminal tab:

celery -A app.worker.celery_app worker --loglevel=info


You should see:

[tasks]
  . app.worker.celery_app.send_notification


✅ Keep this terminal open — this process listens for queued tasks.

🧩 Step 3 — Start the FastAPI Application

In a separate terminal:

python3 -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000


Expected log:

INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)


✅ Keep this terminal open — this is your API server.