from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login
from django.contrib import messages


def home(request):
    return render(request, 'myapp/WelcomePage.html') 

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'myapp/login.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()    
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
