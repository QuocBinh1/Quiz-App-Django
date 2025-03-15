#quiz/views.py
from django.urls import path
from .views import quiz, submit_quiz
from result.views import result


urlpatterns = [
    path('', quiz, name='quiz'),
    path("submit_quiz/", submit_quiz, name="submit_quiz"),
    path("quiz/result/<str:studentId>/", result, name="result"),
]

