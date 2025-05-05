from django.db import models
from django.contrib.auth.models import User, AbstractUser,PermissionsMixin, BaseUserManager

class CustomUserManager(BaseUserManager):
  def create_user(self, username, email=None, password=None, **extra_fields):
    if not username:
      raise ValueError('O campo username é obrigatório.')
    
    email = self.normalize_email(email)
    user = self.model(username=username, email=email, **extra_fields)

    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, username, email=None, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)

    if not extra_fields.get('is_staff'):
      raise ValueError('Superusuário precisa de is_staff=True')
    if not extra_fields.get('is_superuser'):
      raise ValueError('Superusuário precisa de is_superuser=True')


# Create your models here.
class CustomUser(AbstractUser):
    name_user = models.CharField(max_length=200, blank=True)
    telefone = models.CharField(max_length=11, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.email


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