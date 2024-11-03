from django.urls import path,include 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login.html', views.login, name='login'),
    path('registerpage.html', views.register, name='register'),
    path('Mainmenu.html', views.mainmenu, name='mainmenu'),
    path('ParentOrChild.html', views.parentorchild, name='parentorchild'),
    path('Forgot_pass.html', views.forgotpass, name='forgot_password'),
    path('LanguageTranslator.html', views.langtrans, name='langtrans'),
    path('profile.html', views.profile, name='profile'),
    path('Quiz1.html', views.quiz1, name='quiz1'),
    path('Quiz2.html', views.quiz2, name='quiz2'),
    path('score1.html', views.score1, name='score1'),
    path('score2.html', views.score2, name='score2'),
    path('settings.html', views.settings, name='settings'),
    path('Trail.html', views.trail, name='trail'), 
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]
