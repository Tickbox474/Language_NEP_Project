from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import RegistrationForm, LoginForm

def home(request):
    return render(request, 'myapp/WelcomePage.html') 

def login(request):
    return render(request, 'myapp/login.html')     

def register(request):
    return render(request, 'myapp/registerpage.html')          

def mainmenu(request):
    return render(request, 'myapp/Mainmenu.html')

def parentorchild(request):
    return render(request, 'myapp/ParentOrChild.html')

def forgotpass(request):
    return render(request, 'myapp/Forgot_pass.html')

def langtrans(request):
    return render(request, 'myapp/LanguageTranslator.html')

def profile(request):
    return render(request, 'myapp/profile.html')

def quiz1(request):
    return render(request, 'myapp/Quiz1.html')

def quiz2(request):
    return render(request, 'myapp/Quiz2.html')

def score1(request):
    return render(request, 'myapp/score1.html')

def score2(request):
    return render(request, 'myapp/score2.html')

def settings(request):
    return render(request, 'myapp/settings.html')

def trail(request):
    return render(request, 'myapp/Trail.html')
