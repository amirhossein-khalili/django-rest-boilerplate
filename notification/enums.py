from enum import Enum

from django.db import models


class NotificationType(Enum):
    EMAIL = "email"
    SMS = "sms"
    PUSH = "push"
    DEBUG = "debug"


class NotificationChoices(models.TextChoices):
    EMAIL = NotificationType.EMAIL.value, "E"
    SMS = NotificationType.SMS.value, "S"
    PUSH = NotificationType.PUSH.value, "P"
    DEBUG = NotificationType.DEBUG.value, "D"
