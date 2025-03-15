from django.conf import settings

from notification.factories.dev_factory import DevNotificationFactory
from notification.factories.email_factory import EmailNotificationFactory
from notification.factories.push_factory import PushNotificationFactory
from notification.factories.sms_factory import SMSNotificationFactory

from .models import NotificationType


def notification_service(notification_type=None):
    """
    Provides a notification factory instance based on the provided type,
    or falls back to the default type specified in settings.

    This function abstracts the internal factory selection so that other
    applications can use a simple interface. In development mode (DEBUG=True),
    if 'debug' is specified as the notification type, it returns the development
    notification service which prints notifications to the terminal.

    :param notification_type: Optional; desired notification type ("email", "sms", "push", "debug").
    :return: An instance of a NotificationFactory or a NotificationService (for debug).
    """

    # type_str = (
    #     notification_type or getattr(settings, "DEFAULT_NOTIFICATION_TYPE", "email")
    # ).lower()

    # try:
    #     notification_type = NotificationType(type_str)
    # except ValueError:
    #     raise ValueError(f"Invalid notification type '{type_str}' specified")

    if notification_type == NotificationType.EMAIL:
        return EmailNotificationFactory().create_notification_service()
    elif notification_type == NotificationType.PUSH:
        return PushNotificationFactory().create_notification_service()
    elif notification_type == NotificationType.SMS:
        return SMSNotificationFactory().create_notification_service()
    elif notification_type == NotificationType.EMAIL and settings.DEBUG == True:
        return DevNotificationFactory().create_notification_service()
    else:
        raise ValueError(f"Invalid notification type '{type_str}' specified")
