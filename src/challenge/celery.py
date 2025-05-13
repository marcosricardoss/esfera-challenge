from celery import Celery

celery_app = Celery(
    "challenge",
    broker="redis://app.redis:6379/0",
    backend="redis://app.redis:6379/0",
    include=["challenge.tasks"],
)

celery_app.conf.task_routes = {
    "challenge.tasks.create_user_task": {"queue": "users"},
    "user_created_event": {"queue": "events"},
}
