from django.urls import include, path
from rest_framework.routers import DefaultRouter

from notification.views import NotificationViewSet

router = DefaultRouter()
router.register(r"notifications", NotificationViewSet, basename="notification")

app_name = "notification"
urlpatterns = [
    path("", include(router.urls)),
]
