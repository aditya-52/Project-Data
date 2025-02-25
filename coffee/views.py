from django.shortcuts import render
from django.http import HttpResponse
from .models import Coffee

def home(request):
    coffee = Coffee.objects.all()
    return render(request, 'home.html', {'coffee': coffee})
    #return HttpResponse('<h1>Home Page</h1>')


def SignupPage(request):
    return render(request, 'signup.html')

def LoginPage(request):
    return render(request, 'login.html')