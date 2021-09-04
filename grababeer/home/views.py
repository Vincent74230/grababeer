from django.shortcuts import render
from django.http import HttpResponse
from .fetchbeers import beers
 
def index(request):
    page = request.GET.get('page')
    if not page:
        page=1
    page = int(page)
    if page <= 0:
        page = 1

    list_of_beers = beers(page)

    context = {
    'page':page,
    'list_of_beers':list_of_beers,
    }

    return render(request, 'home/index.html', context)
