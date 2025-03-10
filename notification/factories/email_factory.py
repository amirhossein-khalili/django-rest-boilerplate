from notification.factories.notification_factory import NotificationFactory
from notification.services.email_service import EmailNotificationService


class EmailNotificationFactory(NotificationFactory):
    """
    Factory for creating an Email Notification Service.
    """

    def create_notification_service(self) -> EmailNotificationService:
        return EmailNotificationService()
