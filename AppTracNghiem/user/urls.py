from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path('submit_login/', views.submit_login, name='submit_login'), 
]