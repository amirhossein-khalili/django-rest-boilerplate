from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from notification.factories.factory_selector import get_notification_factory
from notification.models import Notification
from notification.serializers import NotificationSerializer


class NotificationViewSet(viewsets.ViewSet):
    """
    API endpoints for sending and listing notifications.
    """

    def list(self, request):
        """
        Retrieve a list of sent notifications.
        """
        notifications = Notification.objects.all().order_by("-sent_at")
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["post"])
    def send(self, request):
        """
        Send a notification via Email, SMS, or Push.

        Example JSON request:
        {
            "recipient": "recipient@example.com",
            "message": "Hello, this is a test notification!"
        }
        """
        recipient = request.data.get("recipient")
        message = request.data.get("message")

        if not recipient or not message:
            return Response(
                {"error": "Recipient and message are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Get the notification factory based on settings
        factory = get_notification_factory()
        notification_service = factory.create_notification_service()

        # Send the notification
        notification_service.send_notification(recipient, message)

        return Response(
            {"success": "Notification sent successfully."}, status=status.HTTP_200_OK
        )
