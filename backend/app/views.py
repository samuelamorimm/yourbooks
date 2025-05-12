from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import RegisterUserSerializer, ClientSerializer, AuthorSerializer, BookSerializer
from .models import Client, Author, Book

# Create your views here.
class AuthorViewSet(ModelViewSet):
  queryset = Author.objects.all()
  serializer_class = AuthorSerializer
  permission_classes = [IsAuthenticated]
  

class CLientViewSet(ModelViewSet):
  queryset = Client.objects.all()
  serializer_class = ClientSerializer
  permission_classes = [IsAuthenticated]

class BookViewSet(ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticated]

class SearchBooksViewSet(ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticated]

  def get_queryset(self):
      nome = self.request.query_params.get('nome')
      author = self.request.query_params.get('author')
      if nome:
        nome = nome.strip().lower()
        queryset = Book.objects.filter(title__icontains=nome)
        if queryset.exists():
          return queryset
        
      if author:
        author = author.strip().lower()
        queryset = Book.objects.filter(author__name_author__icontains=author)
        return queryset
  

class CustomAuthToken(ObtainAuthToken):
  def post(self, request, *args, **kwargs):
    serializer = self.serializer_class(data=request.data, context={'request': request})

    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token, created = Token.objects.get_or_create(user=user)
    return Response({
      'token': token.key,
      'user_id': user.id,
      'username': user.username,
      'email': user.email,
    })
  
class RegisterView(APIView):
  def post(self, request):
    serializer = RegisterUserSerializer(data=request.data)

    if serializer.is_valid():
      user = serializer.save()
      return Response({
        "msg": 'Usuario criado com sucesso!',
        "user": RegisterUserSerializer(user).data
      }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)