from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import CustomAuthToken, RegisterView, AuthorViewSet, CLientViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'clients', CLientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', CustomAuthToken.as_view()),
    path('register/', RegisterView.as_view())
]