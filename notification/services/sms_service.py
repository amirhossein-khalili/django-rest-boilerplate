from typing import Dict, List

from notification.enums import NotificationType
from notification.models import Notification
from notification.services.base import NotificationService
from notification.services.sms_providers.base_sms_provider import BaseSMSProvider


class SMSNotificationService(NotificationService):
    """
    Concrete implementation of NotificationService for sending SMS using a provider.
    """

    NOTIFICATION_TYPE = NotificationType.SMS.value

    def __init__(self, sms_provider: BaseSMSProvider):
        """
        Initialize the SMS service with a provider.

        :param sms_provider: An instance of a class that implements BaseSMSProvider.
        """
        self.sms_provider = sms_provider

    def _send(self, recipient: str, message: str) -> bool:
        """
        Sends an SMS using the configured provider.
        """
        return self.sms_provider.send_sms(recipient, message)
