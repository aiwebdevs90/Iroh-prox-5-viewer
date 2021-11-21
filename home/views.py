from django.shortcuts import render

# Create your views here.


def index(request):
    """ A View to return the index page """
    return render(request, 'home/index.html')


def about(request):
    """ A View to return the index page """
    return render(request, 'home/about.html')


def services(request):
    """ A View to return the index page """
    return render(request, 'home/services.html')


def prox5(request):
    """ A View to return the index page """
    return render(request, 'home/prox5.html')


def photogrammetry(request):
    """ A View to return the index page """
    return render(request, 'home/photogrammetry.html')


def telecomsdatabase(request):
    """ A View to return the index page """
    return render(request, 'home/telecomsdatabase.html')
