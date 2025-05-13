from celery import Celery
from challenge.config import RATE_LIMIT

celery_app = Celery(
    "challenge",
    broker="redis://app.redis:6379/0",
    backend="redis://app.redis:6379/0",
    include=["challenge.tasks"],
)

celery_app.conf.task_routes = {
    "challenge.tasks.create_user_task": {"rate_limit": RATE_LIMIT}
}
