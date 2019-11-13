from django.urls import path

from . import views

urlpatterns = [
    path('', views.homeList, name='homes'),
    path('<int:home_id>', views.home, name='home'),
    path('lookup', views.lookup, name='lookup'),
    path('seller', views.seller, name='seller')

]