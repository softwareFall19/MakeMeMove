from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegisterForm()

    return render(request, "userprofiles/signup.html", {"form":form})


def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            form.save()


            return redirect("signin")
    else:
        form = AuthenticationForm()

    return render(request, "userprofiles/signin.html", {"form":form})

def signout(request):
    return render(request, 'index')
