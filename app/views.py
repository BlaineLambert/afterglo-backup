from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

def homePage(request:HttpRequest)->HttpResponse:
    context = {}
    return render(request, "home.html", context)