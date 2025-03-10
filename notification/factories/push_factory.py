from notification.factories.notification_factory import NotificationFactory
from notification.services.push_service import PushNotificationService


class PushNotificationFactory(NotificationFactory):
    """
    Factory for creating a Push Notification Service.
    """

    def create_notification_service(self) -> PushNotificationService:
        return PushNotificationService()
