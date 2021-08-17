from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *

"""Форма для регистрации"""
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин',widget=forms.TextInput(attrs={'class':'form-input'}))
    password1 = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повторите пароль',widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    email = forms.CharField(label='Почта',widget=forms.EmailInput(attrs={'class': 'form-input'}))
    class Meta:
        model = User
        fields = ['username','password1','password2','email']
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),

        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name_blog','athor_blog']


class SummClientForm(ModelForm):
    class Meta:
        model = SummClientItog
        fields = ['sum_client']

