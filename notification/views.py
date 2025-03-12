from rest_framework import pagination, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from notification.models import Notification
from notification.serializers import NotificationSerializer


class NotificationPagination(pagination.PageNumberPagination):
    """
    Custom pagination for notifications.
    """

    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50


class NotificationViewSet(viewsets.ViewSet):
    """
    API endpoints for listing notifications.
    Users can only see their own notifications.
    """

    permission_classes = [permissions.IsAuthenticated]
    pagination_class = NotificationPagination

    def list(self, request):
        """
        Retrieve a paginated list of sent notifications for the authenticated user.
        """
        notifications = Notification.objects.filter(
            recipient=request.user.email
        ).order_by("-sent_at")

        paginator = self.pagination_class()
        paginated_notifications = paginator.paginate_queryset(notifications, request)

        serializer = NotificationSerializer(paginated_notifications, many=True)
        return paginator.get_paginated_response(serializer.data)
