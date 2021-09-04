from django.shortcuts import render, redirect
from django.http import HttpResponse
from .grababeer_extends import beers, single_beer
 
def index(request):
    page=1

    page = request.GET.get('page')

    if not page:
        page = 1

    list_of_beers = beers(page)

    context = {
    'page':page,
    'list_of_beers':list_of_beers,
    }

    return render(request, 'home/index.html', context)

def save_favourite(request):
    beer = request.GET.get('favourite_beer')
    single_beer(beer)

    return redirect("/")
