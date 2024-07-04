from django.urls import path
from rest_framework.authtoken import views as auth_token_views
from rest_framework import routers


from . import views

app_name = "accounts"
urlpatterns = [
    path("register/", views.UserRegister.as_view()),
    path("auth-token/", auth_token_views.obtain_auth_token),
]


router = routers.SimpleRouter()
router.register("user", views.UserViewSet)
urlpatterns += router.urls
