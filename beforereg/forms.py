from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.EmailInput)

  #  class Meta:
      #  model = User
      #  fields = ['username', 'password1', 'password2', 'email', 'skills', 'branch']
