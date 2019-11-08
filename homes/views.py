from django.shortcuts import render
from .models import Home



# Create your views here.

def index(request):

    homes = Home.objects.all()

    

    context = {
        'homes': homes
    }

    return render(request, 'home_listings/homes.html', context)
    
def home(request):

    homes = Home.objects.all()

    

    context = {
        'homes': homesHome.objects.order_by('-date_posted')
    }
    return render(request, 'home_listings/home.html', context)


def lookup(request):
    homes = Home.objects.all()

    if 'city' in request.GET:
        city = request.GET['city']

        if city:




    context = {
        'homes': homes
    }

    return render(request, 'home_listings/lookup.html', context)

