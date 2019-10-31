from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    if request.method == 'Post':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']

        if password == confirmPassword:
            if User.objects.filter(username = username).exists():
                messages.error(request, "This user already exists")
                return redirect('signup')
            else:
                if User.objects.filter(email = email).exists():
                    messages.error(request, "This email already exists")
                    return redirect('signup')
                else:
                    return
                # kk

        else:
            messages.error(request, "The passwords are different")
            return redirect('signup')
        
    else:
        return render(request, 'userprofiles/signup.html')

def signin(request):
    return render(request, 'userprofiles/signin.html')

def signout(request):
    return redirect('index')