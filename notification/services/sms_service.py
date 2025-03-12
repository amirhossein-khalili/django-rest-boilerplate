from typing import Dict, List

from notification.enums import NotificationType
from notification.models import Notification
from notification.services.base import NotificationService
from notification.services.sms_providers.base_sms_provider import BaseSMSProvider


class SMSNotificationService(NotificationService):
    """
    Concrete implementation of NotificationService for sending SMS using a provider.
    """

    def __init__(self, sms_provider: BaseSMSProvider):
        """
        Initialize the SMS service with a provider.

        :param sms_provider: An instance of a class that implements BaseSMSProvider.
        """
        self.sms_provider = sms_provider

    def send_notification(self, recipient: str, message: str) -> None:
        """
        Sends an SMS notification using the configured provider.

        :param recipient: The recipient's phone number.
        :param message: The SMS content.
        """
        status = self.sms_provider.send_sms(recipient, message)

        Notification.objects.create(
            recipient=recipient,
            message=message,
            notification_type=NotificationType.SMS.value,
            status=status,
        )

    def list_notifications(self) -> List[Dict[str, str]]:
        """
        Retrieve a list of sent SMS notifications.

        :return: A list of dictionaries containing notification details.
        """
        notifications = Notification.objects.filter(
            notification_type=NotificationType.SMS.value
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
