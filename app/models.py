from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    desc = models.TextField()
    photo = models.ImageField(upload_to="app/uploads/", null=True, blank=True, default='app/uploads/default.png')

class User(models.Model):
    name = models.TextField()
    email = models.EmailField()
    number = models.TextField()