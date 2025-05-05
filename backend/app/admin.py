from django.contrib import admin
from .models import Client, Author, Book, Lending

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Client)
admin.site.register(Lending)