from django.urls import path

from . import views

urlpatterns = [
    path('info', views.infoHome, name='info'),
    path('info_rental', views.infoRental, name='info_rental')
]