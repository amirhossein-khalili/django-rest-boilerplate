from django.urls import path

from . import views

app_name = "home"
urlpatterns = [
    path("", views.Home.as_view()),
    path("questions", views.QuestionView.as_view()),
    path("questions/<int:pk>", views.QuestionView.as_view()),
    path("answers", views.AnswerView.as_view()),
    path("answers/<int:pk>", views.AnswerView.as_view()),
]
