from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import CustomAuthToken, RegisterView, AuthorViewSet, CLientViewSet, BookViewSet, SearchBooksViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'clients', CLientViewSet)
router.register(r'books', BookViewSet)
router.register(r'search', SearchBooksViewSet, basename='book-search')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', CustomAuthToken.as_view()),
    path('register/', RegisterView.as_view())
]