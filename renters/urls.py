from django.urls import path

from . import views

urlpatterns = [
    path('', views.rentals, name='renters'),
    path('<int:rental_id>', views.rental, name='rental'),
    path('search', views.search, name='search')

]