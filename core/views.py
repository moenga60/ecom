from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'core/index.html')

def shop(request):
    return render(request, 'core/shop.html')

def aboutus(request):
    return render(request, 'core/about.html')

def services(request):
    return render(request, 'core/services.html')

def blog(request):
    return render(request, 'core/blog.html')

def contactus(request):
    return render(request, 'core/contact.html')

def thankyou(request):
    return render(request, 'core/thankyou.html')

def checkout(request):
    return render(request, 'core/checkout.html')