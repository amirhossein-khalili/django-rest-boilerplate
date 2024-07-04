from django.urls import path
from rest_framework import routers

from . import views

app_name = "accounts"
urlpatterns = [
    path("register/", views.UserRegister.as_view()),
]


router = routers.SimpleRouter()
router.register("user", views.UserViewSet)
urlpatterns += router.urls
