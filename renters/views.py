from django.shortcuts import render, redirect, get_object_or_404

from . models import Rental
from django.db.models import Q


# Create your views here.

def rentals(request):

    rentals = Rental.objects.all()

    context = {
        'rentals': rentals
    }

    return render(request, 'rentals/rentals.html', context)
    
def rental(request, rental_id):

    rental = get_object_or_404(Rental, pk=rental_id)

    context = {
        'rental': rental
    }

    
    return render(request, 'rentals/rental.html', context)


def search(request):
    rental_search = Rental.objects.all()

    srch = request.GET.get("search")
    if srch:
        rental_search = rental_search.filter(
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
        'rentals': rental_search
    }

    return render(request, 'rentals/search.html', context)


