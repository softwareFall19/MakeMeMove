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
    return render(request, 'home_listings/home.html')


def lookup(request):
    return render(request, 'home_listings/lookup.html')

