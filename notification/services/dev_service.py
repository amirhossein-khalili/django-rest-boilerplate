from datetime import datetime
from typing import Dict, List

from notification.services.base import NotificationService


class DevNotificationService(NotificationService):
    """
    A development notification service that prints notifications to the terminal.
    This service is used only when DEBUG is True.
    """

    def __init__(self):
        self.notifications = []

    def send_notification(self, recipient: str, message: str) -> None:
        """
        Print the notification to the terminal and store it in memory.
        """
        print("=======================")
        print(f"[DEV] Notification to {recipient}")
        print("=======================")
        print(message)
        print("=======================")
        self.notifications.append(
            {
                "recipient": recipient,
                "message": message,
                "sent_at": datetime.now(),
                "status": "Printed",
            }
        )

    def _send(self, recipient, message):
        pass

    def list_notifications(self) -> List[Dict[str, str]]:
        """
        Retrieve a list of notifications that were 'sent' (printed) in development.
        """
        print("=======================")
        print("== notification list ==")
        print("=======================")
        print(self.notifications)
        print("=======================")
