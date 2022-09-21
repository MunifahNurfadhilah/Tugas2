from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    watchlist = MyWatchList.objects.all()
    context = {
    'list_mywatchlist': watchlist,
    'nama': 'pudil',
    'npm' : '2106654851',
    'notification' : ""
    }

    film_watched = 0
    film_not_watched = 0
    for films in watchlist :
        if (films.watched_film == "Sudah") :
            film_watched += 1
        else :
            film_not_watched += 1
    
    if (film_watched >= film_not_watched) :
        context['notification'] = "Selamat, kamu sudah banyak menonton!"
    else :
        context['notification'] = "Wah, kamu masih sedikit menonton!"

    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")