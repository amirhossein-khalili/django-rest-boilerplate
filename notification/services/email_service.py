from typing import Dict, List

from django.conf import settings
from django.core.mail import send_mail

from notification.models import Notification
from notification.services.base import NotificationService


class EmailNotificationService(NotificationService):
    """
    Concrete implementation of NotificationService for sending emails.
    """

    def send_notification(self, recipient: str, message: str) -> None:
        """
        Send an email notification.

        :param recipient: The recipient's email address.
        :param message: The email content.
        """
        subject = "New Notification"
        from_email = settings.DEFAULT_FROM_EMAIL  # Ensure this is set in settings.py

        try:
            send_mail(subject, message, from_email, [recipient])
            Notification.objects.create(
                recipient=recipient,
                message=message,
                notification_type=Notification.EMAIL,
                status=True,
            )
        except Exception as e:
            # Log the error (optional)
            print(f"Failed to send email: {e}")
            Notification.objects.create(
                recipient=recipient,
                message=message,
                notification_type=Notification.EMAIL,
                status=False,
            )

    def list_notifications(self) -> List[Dict[str, str]]:
        """
        Retrieve a list of sent email notifications.

        :return: A list of dictionaries containing notification details.
        """
        notifications = Notification.objects.filter(
            notification_type=Notification.EMAIL
        ).order_by("-sent_at")
        return [
            {
                "recipient": n.recipient,
                "message": n.message,
                "sent_at": n.sent_at.strftime("%Y-%m-%d %H:%M:%S"),
                "status": "Sent" if n.status else "Failed",
            }
            for n in notifications
        ]
