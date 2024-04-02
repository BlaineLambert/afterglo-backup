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

def testing(request:HttpRequest) -> HttpResponse:
    form1 = CreateUser
    form2 = ListProduct
    if request.method == 'POST':
        print("hello")
        if 'user' in request.POST:
            form1 = CreateUser(request.POST)
            if form1.is_valid():
                form1.save()
        if 'product' in request.POST:
            form2 = ListProduct(request.POST, request.FILES)
            if form2.is_valid():
                form2.save()
        if 'delete_product' in request.POST:
            print("hello")
            product_id = request.POST['delete_product']
            product_to_delete = get_object_or_404(Product, id=product_id)
            product_to_delete.delete()

    products = Product.objects.all()
    context = {'form1': form1, 'form2': form2, 'products': products}
    return render(request, "test.html", context)