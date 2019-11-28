from django.shortcuts import render, redirect, get_object_or_404

from .models import Home
from django.db.models import Q
from .forms import SellerForm
from django.contrib.auth.decorators import login_required





# Create your views here.

def homeList(request):

    homes = Home.objects.all()

    context = {
        'homes': homes
    }

    return render(request, 'home_listings/homes.html', context)
    
def home(request, home_id):

    home = get_object_or_404(Home, pk=home_id)

    context = {
        'home': home
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



def seller(request): 
    if request.method == 'POST':
        form = SellerForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('homes')
    else:
        form = SellerForm()

    return render(request, 'sellers/seller_form.html', {
        'form': form
    })