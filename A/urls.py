from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls", namespace="home")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
]
