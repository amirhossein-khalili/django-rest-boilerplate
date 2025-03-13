from django.conf import settings
from django.core.mail import send_mail

from notification.enums import NotificationType
from notification.services.base import NotificationService
from notification.services.mixins import NotificationMixin


class EmailNotificationService(NotificationService, NotificationMixin):
    """
    Sends email notifications.
    """

    NOTIFICATION_TYPE = NotificationType.EMAIL.value

    def _send(self, recipient: str, message: str) -> bool:
        """
        Sends an email using Django's email backend.
        """
        subject = setting.DEFAULT_SUBJECT_EMAIL
        from_email = settings.DEFAULT_FROM_EMAIL

        try:
            send_mail(subject, message, from_email, [recipient])
            return True
        except Exception as e:
            print(f"Failed to send email: {e}")
            return False
