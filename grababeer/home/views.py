from django.shortcuts import render, redirect
from django.http import HttpResponse
from .grababeer_extends import beers, single_beer
 
def index(request):

    pagination = request.GET.get('pagination')
    if not pagination:
        page = 1
        list_of_beers = beers(page)
        context = {
        'page':page,
        'list_of_beers':list_of_beers,
        }
        return render(request, 'home/index.html', context)
    else:
        page = request.GET.get('page')
        page = int(page)
        pagination = request.GET.get('pagination')
        if pagination == 'previous':
            page -= 1
        else:
            page += 1

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
