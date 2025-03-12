from django.test import TestCase, override_settings

from notification.factories.dev_factory import DevNotificationFactory
from notification.factories.email_factory import EmailNotificationFactory
from notification.factories.push_factory import PushNotificationFactory
from notification.factories.sms_factory import SMSNotificationFactory
from notification.provider import notification_service


class NotificationServiceFactoryTest(TestCase):

    @override_settings(DEBUG=False, DEFAULT_NOTIFICATION_TYPE="email")
    def test_email_notification_factory(self):
        factory = notification_service("email")
        self.assertIsInstance(factory, EmailNotificationFactory)

    @override_settings(DEBUG=False)
    def test_sms_notification_factory(self):
        factory = notification_service("sms")
        self.assertIsInstance(factory, SMSNotificationFactory)

    @override_settings(DEBUG=False)
    def test_push_notification_factory(self):
        factory = notification_service("push")
        self.assertIsInstance(factory, PushNotificationFactory)

    @override_settings(DEBUG=True)
    def test_debug_notification_service_in_debug_mode(self):
        # When DEBUG is True and "debug" is passed,
        # notification_service returns a notification service instance
        # created by DevNotificationFactory().create_notification_service()
        service = notification_service("debug")
        # For example, you might expect this service to have a "send_notification" method.
        self.assertTrue(hasattr(service, "send_notification"))

    @override_settings(DEBUG=False)
    def test_debug_notification_invalid_in_non_debug_mode(self):
        # When DEBUG is False, "debug" is not a valid type.
        with self.assertRaises(ValueError):
            notification_service("debug")

    @override_settings(DEBUG=False)
    def test_invalid_notification_type(self):
        with self.assertRaises(ValueError):
            notification_service("invalid")
