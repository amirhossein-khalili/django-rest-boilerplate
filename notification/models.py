from django.db import models


class Notification(models.Model):
    EMAIL = "email"
    SMS = "sms"
    PUSH = "push"

    NOTIFICATION_TYPES = [
        (EMAIL, "Email"),
        (SMS, "SMS"),
        (PUSH, "Push Notification"),
    ]

    recipient = models.CharField(
        max_length=255, help_text="Recipient's email, phone number, or device ID"
    )
    message = models.TextField(help_text="Notification content")
    notification_type = models.CharField(
        max_length=10, choices=NOTIFICATION_TYPES, help_text="Type of notification"
    )
    sent_at = models.DateTimeField(
        auto_now_add=True, help_text="Timestamp when the notification was sent"
    )
    status = models.BooleanField(
        default=False, help_text="Delivery status: True if sent successfully"
    )

    def __str__(self):
        return f"{self.get_notification_type_display()} to {self.recipient} at {self.sent_at}"

    class Meta:
        ordering = ["-sent_at"]
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
