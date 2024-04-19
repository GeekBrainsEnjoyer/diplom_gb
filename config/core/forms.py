from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


INPUT_CLASSES = 'w-full py-2 px-7 rounded-xl'


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Input your username',
        'class': INPUT_CLASSES
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Input your password',
        'class': INPUT_CLASSES
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Input your username',
        'class': INPUT_CLASSES
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Input your email address',
        'class': INPUT_CLASSES
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Input your password',
        'class': INPUT_CLASSES
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat your password',
        'class': INPUT_CLASSES}))
