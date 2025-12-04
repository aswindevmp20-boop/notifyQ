from celery import Celery
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery(
    "notify_tasks",
    broker=REDIS_URL,
    backend=REDIS_URL
)

@celery_app.task(bind=True)
def send_notification(self, email: str, message: str):
    print(f"Sending notification to {email}:{message}")
    return {"email": email, "message": message}



#Start Celery Worker
# celery -A app.worker.celery_app worker --loglevel=info


#Start FastAPI app
#python3 -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
