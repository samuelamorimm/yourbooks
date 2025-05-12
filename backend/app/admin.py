from django.contrib import admin
from .models import Client, Author, Book, Lending, User

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Client)
admin.site.register(Lending)
admin.site.register(custom)