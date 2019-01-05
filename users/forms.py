from django import forms
from django.contrib.auth.models import  User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:#this class gives us the nested namespace for configuration and keeps the confuguration in one place
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#form to update the user model

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:  # this class gives us the nested namespace for configuration and keeps the confuguration in one place
        model = User
        fields = ['username', 'email']

class ProfileUpdateFrom(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
