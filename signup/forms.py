from typing import Any
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    fname = forms.CharField(widget=forms.TextInput(attrs={'name':'fname', 'required':'true', 'placeholder':'First Name', 'class':'field-input'}))
    lname = forms.CharField(widget=forms.TextInput(attrs={'name':'lname', 'required':'false', 'onclick':'hint_function()', 'placeholder':'Last Name (optional)', 'class':'field-input'}))
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'name':'uname', 'required': 'true', 'placeholder':'User Name', 'class':'field-input'}), )
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'name':'email', 'placeholder':'Email address', 'required':'true', 'class':'field-input'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'name':'pswd', 'required':'true', 'placeholder': 'Set a new password', 'class':'field-input'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'name':'pswd-repeat', 'required':'true', 'placeholder':'Confirm your password', 'class':'field-input'}))

    class Meta:
        model = User
        fields = ('fname', 'lname', 'username','email', 'password1', 'password2', )