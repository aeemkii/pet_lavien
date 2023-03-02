from django import forms

from django.contrib.auth.forms import UserCreationForm
from apps.accounts.models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Имя пользователя",
        widget= forms.TextInput(attrs={"class":"form-control", "placeholder":"exapmle0_1"})
    )
    password = forms.CharField(
        label="Пароль",
        widget= forms.PasswordInput(attrs={"class":"form-control", "placeholder":"example000"})
    )

forms.ModelForm

class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"name"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"name"}))


    class Meta:
        model = User
        fields = [
            "username", 
            "first_name", 
            "last_name", 

        ]
