from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login,logout, authenticate

from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from userprofiles.models import Profile
from django.core.mail import EmailMessage
from django.conf import settings
import stripe 
from django.views.generic.base import TemplateView
from .forms import RegisterForm, ProfileForm, LoginForm


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'You are registered, {username}')
            return redirect('signin')
            user_form = RegisterForm(data=request.POST)
            profile_form = ProfileForm(data=request.POST)
            if user_form.is_valid() and profile_form.is_valid():
                #username = form.cleaned_data.get('username')
                user = user_form.save()
                user.set_password(user.password)
                user.is_active = False
                user.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                current_site = get_current_site(request)
                subject = 'Thank you for registering with use. Please activate your account.'
                message = render_to_string('userprofiles/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
                user.email_user(subject, message)
                return render(request, "userprofiles/account_activation_sent.html")
    else:
        form = RegisterForm()

    return render(request, "userprofiles/signup.html", {"form":form})


def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # return redirect('index')
            return render(request, "userprofiles/user_home.html")
    else:
        form = AuthenticationForm()

    return render(request, "userprofiles/signin.html", {"form":form})

def signout(request):

    logout(request)
    return redirect('index')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can login to your account.')
    else:
        return HttpResponse('Activation link is invalid!')

class UserProfileView(TemplateView):
    template_name = 'userprofiles/user_home.html'

    def user_profile(request):
        return redirect('userprofiles/user_home.html')

    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

def charge(request): # new
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='Pay',
            source=request.POST['stripeToken']
        )
        return redirect('thankyou_payment')
    else:
        return redirect('user_home')


