from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 24)
    price = models.IntegerField()
    desc = models.CharField(max_length = 255)
    photo = models.ImageField(upload_to="app/uploads/", null=True, blank=True, default='app/uploads/default.png')

class User(models.Model):
    fname = models.CharField(max_length = 24)
    lname = models.CharField(max_length = 24)
    email = models.EmailField()
    number = models.CharField(max_length = 10)