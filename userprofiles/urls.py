from django.urls import path
from django.urls import path, include
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout')

]