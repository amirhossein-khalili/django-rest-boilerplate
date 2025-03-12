from typing import Dict, List

import requests
from django.conf import settings

from notification.models import Notification
from notification.enums import NotificationType
from notification.services.base import NotificationService


class PushNotificationService(NotificationService):
    """
    Concrete implementation of NotificationService for sending push notifications via Firebase Cloud Messaging (FCM).
    """

    def __init__(self):
        """
        Initializes Firebase FCM API credentials.
        """
        self.fcm_api_url = "https://fcm.googleapis.com/fcm/send"
        self.fcm_server_key = settings.FCM_SERVER_KEY

    def send_notification(self, recipient: str, message: str) -> None:
        """
        Sends a push notification via Firebase Cloud Messaging (FCM).

        :param recipient: The recipient's device token.
        :param message: The push notification content.
        """
        headers = {
            "Authorization": f"key={self.fcm_server_key}",
            "Content-Type": "application/json",
        }

        data = {
            "to": recipient,  # Device token
            "notification": {"title": "New Notification", "body": message},
        }

        try:
            response = requests.post(self.fcm_api_url, json=data, headers=headers)
            response.raise_for_status()
            success = response.status_code == 200
        except requests.exceptions.RequestException as e:
            print(f"Failed to send push notification: {e}")
            success = False

        Notification.objects.create(
            recipient=recipient,
            message=message,
            notification_type=NotificationType.PUSH.value,
            status=success,
        )

    def list_notifications(self) -> List[Dict[str, str]]:
        """
        Retrieve a list of sent push notifications.

        :return: A list of dictionaries containing notification details.
        """
        notifications = Notification.objects.filter(
            notification_type=NotificationType.PUSH.value,
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
