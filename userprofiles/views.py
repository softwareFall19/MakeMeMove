from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login,logout


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'You are registered, {username}')
            return redirect('signin')
    else:
        form = RegisterForm()

    return render(request, "userprofiles/signup.html", {"form":form})


def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('index')
    else:
        form = AuthenticationForm()

    return render(request, "userprofiles/signin.html", {"form":form})

def signout(request):

    logout(request)
    return redirect('index')
