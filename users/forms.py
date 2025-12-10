from django import forms

from users.models import User
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):

    # without django
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    # with django
    # username = forms.CharField(
    #     label='Username',
    #     widget=forms.TextInput(attrs={"autofocus": True,
    #                                                          "class": "form-control",
    #                                                          "placeholder": "Username"}))
    # password = forms.CharField(
    #     label='Password',
    #     widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
    #                                                              "class": "form-control",
    #                                                              "placeholder": "Password"
    #                                                              }))

    class Meta:
        model = User
        fields = ('username', 'password')
