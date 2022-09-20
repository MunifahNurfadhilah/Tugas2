from django.shortcuts import render
from mywatchlist.models import MyWatchList

# Create your views here.
def show_mywatchlist(request):
    watchlist = MyWatchList.objects.all()
    context = {
    'list_mywatchlist': watchlist,
    'nama': 'pudil',
    'npm' : '2106654851'
}
    return render(request, "mywatchlist.html", context)