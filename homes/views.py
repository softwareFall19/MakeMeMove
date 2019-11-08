from django.shortcuts import render
from .models import Home
from django.db.models import Q



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
        'homes': homes
    }
    return render(request, 'home_listings/home.html', context)


def lookup(request):
    home_search = Home.objects.all()

    srch = request.GET.get("search")
    if srch:
        home_search = home_search.filter(
            Q(city__iexact=srch) |
            Q(state__iexact=srch) |
            Q(zipcode__iexact=srch) |
            Q(address__icontains=srch) |
            Q(address__icontains=srch) |
            Q(property_title__icontains=srch) |
            Q(bedrooms__iexact=srch) |
            Q(bathrooms__iexact=srch)

        )


    context = {
        'homes': home_search
    }

    return render(request, 'home_listings/lookup.html', context)

