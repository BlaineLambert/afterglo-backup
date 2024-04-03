from django.shortcuts import render
from app.models import *
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
import openai
import re
openai.api_key = "API KEY"
def is_allowed_question(question):
    questions = [
    r"skin",
    r"skin care",
    r"lotion",
    r'tan',
    r"tanning",
    r'hello',
    r'goodbye',
    r'thank you'
]
    for pattern in questions:
        if re.search(pattern, question, re.IGNORECASE):
            return True
    
    return False

def response(prompt):
    
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role":"user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()



def load_main(request: HttpRequest):
    form = Chatbot_Form()
    if request.method == "POST":
        form = Chatbot_Form(request.POST)
        if form.is_valid():
            print("something") 
            user_input = form.cleaned_data["user_input"]
            if is_allowed_question(user_input):
                chat_response = response(user_input)
                context = {"form":form,"response":chat_response,'itemsInCart':itemsInCart}
                return render(request, 'home.html', {"form":form,"response":chat_response,"user_input":user_input})
            else:
                chat_response = "Sorry but im here to answer questions about skin care and tanning"
                context = {"form":form,"response":chat_response,'itemsInCart':itemsInCart}
                return render(request, 'home.html', {"form":form,"response":chat_response,"user_input":user_input})
    else:
        context = {}
        return render(request, 'home.html', context)


def homePage(request:HttpRequest)->HttpResponse:
    context = {}
    return render(request, "home.html", context)

def testing(request:HttpRequest) -> HttpResponse:
    form1 = CreateUser
    form2 = ListProduct
    if request.method == 'POST':
        if 'user' in request.POST:
            form1 = CreateUser(request.POST)
            if form1.is_valid():
                form1.save()
        if 'product' in request.POST:
            form2 = ListProduct(request.POST, request.FILES)
            if form2.is_valid():
                form2.save()
        if 'delete_product' in request.POST:
            product_id = request.POST['delete_product']
            product_to_delete = get_object_or_404(Product, id=product_id)
            product_to_delete.delete()
        if 'delete_user' in request.POST:
            user_id = request.POST['delete_user']
            user_to_delete = get_object_or_404(User, id=user_id)
            user_to_delete.delete()

    products = Product.objects.all()
    users = User.objects.all()
    context = {'form1': form1, 'form2': form2, 'products': products, 'users': users}
    return render(request, "test.html", context)


def products(request):
    if request.method == "POST":
        product_id = request.POST.get('buy-product')
        quantity = int(request.POST.get('quantity', 1))  
        if 'cart' not in request.session or not request.session['cart']:
            request.session['cart'] = {}
        cart = request.session['cart']
        if product_id in cart:
            cart[product_id] += quantity
        else:
            cart[product_id] = quantity
        request.session.modified = True
        return redirect('products')  
    else:
        products = Product.objects.all()
        context = {'products': products}
        return render(request, "products.html", context)

def faq(request):
    faqs = [
        {'question': 'How does indoor tanning work?', 'answer': 'Indoor tanning involves using a device that emits ultraviolet radiation to produce a cosmetic tan.'},
        {'question': 'Is indoor tanning safe?', 'answer': 'While indoor tanning can help simulate natural sunlight, it\'s important to use it responsibly to minimize skin damage.'},
        {'question': 'What should I wear for tanning?', 'answer': 'Most people wear swimwear. It\'s important to protect sensitive areas that aren\'t usually exposed to the sun.'},
        {'question': 'How long should my tanning session be?', 'answer': 'Session length can vary depending on your skin type and the intensity of the tanning bed. It\'s best to start with shorter sessions and gradually increase the time.'},
        {'question': 'How can I extend the life of my tan?', 'answer': 'Moisturizing your skin regularly can help extend the duration of your tan. Drinking plenty of water also helps.'},
    ]

    context = {
        "faqs":faqs
    }
    
    return render(request, "faq.html", context)

def blog(request):
    context = {

    }
    return render(request, "blog.html", context)

def payment_packages(request):
    context = {

    }
    return render(request, "payment_packages.html", context)