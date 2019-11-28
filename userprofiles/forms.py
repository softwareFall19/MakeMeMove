from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from userprofiles.models import Profile



class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username","first_name", "last_name", "email", "password1", "password2"]
        # fields = ["username", "email", "password1", "password2"]


class LoginForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('email', 'password')

class ProfileForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta():
        model = Profile
        fields = ('profile_pic',)