from django.urls import path, include

from . import views

urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),


    path('signout', views.signout, name='signout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('user_home', views.UserProfileView.as_view(), name='user_home'),
    #path('make_payment', views.get_context_data, name='make_payment'),
    #path('make_payment', views.PaymentView.as_view(), name='make_payment'),
    path('paymentconfirmation_sent', views.charge, name='paymentconfirmation_sent'),    

]