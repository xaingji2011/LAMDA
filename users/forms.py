from django import forms

from users.models import User
from users.models import CaptchaModel


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=2)
    email = forms.EmailField()
    captcha = forms.CharField(max_length=6, min_length=6)
    password = forms.CharField(max_length=20, min_length=6)



class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20, min_length=6)
    remember = forms.IntegerField(required=False)
