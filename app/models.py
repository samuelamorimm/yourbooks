from django.db import models
from django.contrib.auth.models import User, AbstractUser,PermissionsMixin




# Create your models here.
class CustomUser(AbstractUser, PermissionsMixin):
    name_user = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11, blank=False)

    def __str__(self):
        return self.name_user


class Client(models.Model):
    name_profile = models.CharField(max_length=200, blank=False)
    cpf = models.CharField(max_length=11, blank=False)
    age = models.IntegerField(blank=False)

    def __str__(self):
        return self.name_profile

class Author(models.Model):
    name_author = models.CharField(max_length=200)

    def __str__(self):
        return self.name_author
    
class Book(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Lending(models.Model):
    STATUS_CHOICES = [
        ('E', 'Emprestado'),
        ('D', 'Devolvido'),
        ('A', 'Atraso na devolução'),
    ]

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default='E')