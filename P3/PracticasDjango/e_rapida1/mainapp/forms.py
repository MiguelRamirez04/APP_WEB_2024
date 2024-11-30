from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model=User#se usa para meterse a la tabla como ya existe lo usamos
        fields=['username','email','first_name','last_name','password1','password2']