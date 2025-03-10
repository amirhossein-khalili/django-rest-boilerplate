from abc import ABC, abstractmethod
from typing import Dict, List


class NotificationService(ABC):
    """
    Abstract class for notification services.
    Defines the interface for sending notifications and retrieving sent notifications.
    """

    @abstractmethod
    def send_notification(self, recipient: str, message: str) -> None:
        """
        Send a notification to a recipient.

        :param recipient: The recipient of the notification (email, phone number, etc.).
        :param message: The content of the notification.
        """
        pass

    @abstractmethod
    def list_notifications(self) -> List[Dict[str, str]]:
        """
        Retrieve a list of sent notifications.

        :return: A list of dictionaries containing notification details (e.g., recipient, message, timestamp).
        """
        pass
