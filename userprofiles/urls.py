from django.urls import path
from django.urls import path, include
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('user_home', views.UserProfileView.as_view(), name='user_home'),
    #path('make_payment', views.get_context_data, name='make_payment'),
    #path('make_payment', views.PaymentView.as_view(), name='make_payment'),
    path('thankyou_payment', views.charge, name='thankyou_payment'),
    #path('profile_edit', views.profile_edit, name='profile_edit')
]