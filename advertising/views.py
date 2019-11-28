from django.shortcuts import render, redirect

# from .models import Advertise
from .forms import AdvertiseForm



def advertising(request):
    if request.method == 'POST':
        form = AdvertiseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AdvertiseForm()

    context = {
        'form': form
    }

    return render(request, 'advertising/advertising.html', context)