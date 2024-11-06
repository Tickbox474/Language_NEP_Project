from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Sum
from .models import QuizAnswer
from .models import Score

def home(request):
    return render(request, 'myapp/WelcomePage.html') 

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('mainmenu')  # Make sure 'mainmenu' is the correct URL name for Mainmenu.html
        else:
            # Show an error message
            messages.error(request, "Invalid username or password")
    
    return render(request, 'myapp/login.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        if password1 == password2:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                return redirect("login")  # Redirect to login page
            else:
                messages.error(request, "Username already exists.")
        else:
            messages.error(request, "Passwords do not match.")
    
    return render(request, "myapp/registerpage.html")

@login_required          
def mainmenu(request):
    return render(request, 'myapp/Mainmenu.html')

def parentorchild(request):
    return render(request, 'myapp/ParentOrChild.html')

def forgotpass(request):
    return render(request, 'myapp/Forgot_pass.html')

@login_required
def langtrans(request):
    return render(request, 'myapp/LanguageTranslator.html')

@login_required
def profile(request):
    return render(request, 'myapp/profile.html')

@login_required
def quiz1(request):
    if request.method == 'POST':
        answer = request.POST.get('answer')
        user = request.user

        # Check if the answer is correct
        correct_answer = 'Choice C'  # Replace with the actual correct answer
        if answer == correct_answer:
            # Update score
            score, created = Score.objects.get_or_create(user=user)
            score.points += 1  # Increment score
            score.save()
        
        # Redirect to the next quiz or score page
        return redirect('quiz2')  # Replace with your actual URL name

    return render(request, 'myapp/Quiz1.html')

@login_required
def quiz2(request):
    if request.method == 'POST':
        answer = request.POST.get('answer')
        user = request.user

        # Check if the answer is correct
        correct_answer = 'Choice C'  # Replace with the actual correct answer
        if answer == correct_answer:
            # Update score
            score, created = Score.objects.get_or_create(user=user)
            score.points += 1  # Increment score
            score.save()
        
        # Redirect to the scoreboard or next page
        return redirect('scoreboard')  # Replace with your actual URL name

    return render(request, 'myapp/Quiz2.html')

@login_required
def scoreboard(request):
    top_scores = Score.objects.all().order_by('-points')[:3]
    return render(request, 'myapp/scoreboard.html', {'top_scores': top_scores})

@login_required
def score1(request):
    return render(request, 'myapp/score1.html')

@login_required
def score2(request):
    return render(request, 'myapp/score2.html')

@login_required
def settings(request):
    return render(request, 'myapp/settings.html')

@login_required
def trail(request):
    return render(request, 'myapp/Trail.html')
