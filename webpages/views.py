from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'webpages/index.html')


def about(request):
    return render(request, 'webpages/about.html')


