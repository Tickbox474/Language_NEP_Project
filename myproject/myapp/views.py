from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import RegistrationForm, LoginForm

def home(request):
    return render(request, 'myapp/WelcomePage.html') 

def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('mainmenu')  # Redirect to the main menu after login
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'myapp/login.html', {'form': form})     

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'myapp/registerpage.html', {'form': form})          

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
