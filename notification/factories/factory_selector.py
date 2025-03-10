from django.conf import settings

from notification.factories.email_factory import EmailNotificationFactory
from notification.factories.push_factory import PushNotificationFactory
from notification.factories.sms_factory import SMSNotificationFactory


def get_notification_factory():
    """
    Selects the appropriate notification factory based on settings.

    :return: An instance of NotificationFactory (Email, SMS, or Push).
    """
    notification_type = getattr(settings, "DEFAULT_NOTIFICATION_TYPE", "email").lower()

    if notification_type == "sms":
        return SMSNotificationFactory()
    elif notification_type == "email":
        return EmailNotificationFactory()
    elif notification_type == "push":
        return PushNotificationFactory()
    else:
        raise ValueError(
            f"Invalid notification type '{notification_type}' specified in settings"
        )
