import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")


app.config_from_object("django.conf:settings", namespace="CELERY")


app.autodiscover_tasks()

app.conf.beat_schedule = {
    "delete-expired-otps-every-5-minutes": {
        "task": "accounts.tasks.delete_expired_otps",
        "schedule": 30.0,
    },
}
