from django import forms

from users.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

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


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    first_name = forms.CharField()
    last_name = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()

    # with backend
    # first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    # last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    # password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    # password2 = forms.CharField(
    #     widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'PASSWORD CONFIRMATION'}))
    # username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    # email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'image')
        image = forms.ImageField(required=False)
        first_name = forms.CharField()
        last_name = forms.CharField()
        username = forms.CharField()
        email = forms.CharField()
        # image = cwidget=forms.FileInput(attrs={'class': 'form-control mt-3'}), required=False)
        # first_name = forms.CharField(
        #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
        # last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
        # username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
        # email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'readonly': True}))
