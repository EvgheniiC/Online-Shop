from http.client import HTTPResponse

from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm

from carts.models import Cart


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, f"{username} you was successful logining ")

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

                if request.GET.get('next', None):
                    return HttpResponseRedirect(request.GET.get('next'))
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {"title": "Autorization Page", "form": form}
    return render(request, 'users/login.html', context)


@login_required
def logout(request):
    messages.success(request, f"{request.user.username} you was successful logout")
    auth.logout(request)
    return redirect(reverse('main:index'))


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)

            messages.success(request, f"{user.username} you was successful registered ")
            redirect_page = request.POST.get('next', None)
            if redirect_page and redirect_page != reverse('users:logout'):
                return HttpResponseRedirect(request.POST.get('next'))
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
    context = {"title": "Registration Page", "form": form}
    return render(request, 'users/registration.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user,
                           files=request.FILES)  # Форма будет заполнена и можно туда ложить файл
        if form.is_valid():
            form.save()
            messages.success(request, f"you was successful updated")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)
    context = {"title": "Kabinet Page", "form": form}
    return render(request, 'users/profile.html', context)


def users_cart(request):
    return render(request, 'users/users_cart.html')
