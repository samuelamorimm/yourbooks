from rest_framework import serializers
from .models import CustomUser, Book, Author, Client

class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
  class Meta:
    model = Client
    fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = '__all__'

class RegisterUserSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True) #não mostra a senha na resposta

  class Meta:
    model = CustomUser
    fields = ['username', 'email', 'password', 'name_user', 'telefone', 'data_nascimento']

  def create(self, validated_data):
    user = CustomUser.objects.create_user(
      username=validated_data['username'],
      email=validated_data['email'],
      password=validated_data['password'],
      name_user=validated_data.get('name_user', ''),
      telefone=validated_data.get('telefone', ''),
      data_nascimento=validated_data.get('data_nascimento', None),
    )
    return user