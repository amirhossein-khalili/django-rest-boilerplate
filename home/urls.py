from django.urls import path

from . import views

app_name = "home"
urlpatterns = [
    path("", views.Home.as_view()),
    path("questions/", views.QuestionListView.as_view()),
    path("questions/getData/<int:pk>/", views.QuestionGetDataView.as_view()),
    path("questions/create/", views.QuestionCreateView.as_view()),
    path("questions/update/<int:pk>/", views.QuestionUpdateView.as_view()),
    path("questions/delete/<int:pk>/", views.QuestionDeleteView.as_view()),
    path("answers/", views.AnswerListView.as_view()),
    path("answers/getData/<int:pk>/", views.AnswerGetDataView.as_view()),
    path("answers/create/", views.AnswerCreateView.as_view()),
    path("answers/update/<int:pk>/", views.AnswerUpdateView.as_view()),
    path("answers/delete/<int:pk>/", views.AnswerDeleteView.as_view()),
]
