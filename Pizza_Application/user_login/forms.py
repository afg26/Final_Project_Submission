#importing required libraries 
from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User




#creating our sign up form by using django built in UserCreationForm
#I have added two fields by my own.
#this class is made with all the specifation of the fields and their type
class Add_user(UserCreationForm):
    
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder' : ''}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder' : ''}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder' : ''}))
    password1 = forms.PasswordInput(attrs={'class':'position04', 'placeholder' : ''})
    password2 =forms.PasswordInput(attrs={'class':'position05', 'placeholder' : ''})
    
    class Meta:
        model = User
        fields = [
            'username', "email", 'phone_number',"password1",  "password2"
        ]




   

  