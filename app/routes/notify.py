from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel, EmailStr
from app.worker.celery_app import send_notification
from app.routes.auth import get_current_user
from app.models import User
from app.worker.celery_app import celery_app

router = APIRouter(prefix="/notify", tags=["notifications"])

class NotificationRequest(BaseModel):
    email: EmailStr
    message: str

@router.post("/", status_code=status.HTTP_202_ACCEPTED)
def create_notification(payload: NotificationRequest, current_user: User = Depends(get_current_user)):
    # Enqueue a notification to be processed  asynchronusly

    try:
        task= send_notification.delay(payload.email, payload.message)
        return {"task_id": task.id, "status": "queued"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/status/{task_id}")
def get_notification_status(task_id: str, current_user: User = Depends(get_current_user)):

    #Retrieve Celery task status and result.

    task = celery_app.AsyncResult(task_id)
    print(f"[DEBUG] Task ID: {task_id}, State: {task.state}, Result: {task.result}")
    response = {
        "task_id": task.id,
        "status": task.status,
        "result": task.result if task.successful() else None
    }
    return response