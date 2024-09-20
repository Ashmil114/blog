from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "text-2xl"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": ""}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": ""}))

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]
