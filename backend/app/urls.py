from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import CustomAuthToken, RegisterView

urlpatterns = [
    path('login/', CustomAuthToken.as_view()),
    path('register/', RegisterView.as_view())
]