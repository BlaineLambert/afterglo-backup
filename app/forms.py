from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class CreateUser(ModelForm):
    class Meta:
        model = User
        fields = ['fname', 'lname', 'number', 'email']

class ListProduct(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'photo', 'desc']