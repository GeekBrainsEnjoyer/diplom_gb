from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path(route='singup/', view=views.signup, name='signup'),
    path('login/', auth_view.LoginView.as_view(template_name='core/login.html',
         authentication_form=LoginForm), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name="core/index.html"), name='logout')
    
]
