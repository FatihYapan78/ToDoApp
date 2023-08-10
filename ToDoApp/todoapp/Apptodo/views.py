from django.shortcuts import render, redirect
from .models import *


def index(request):
    films = FilmName.objects.all()
    if request.method == "POST":
        filmname = request.POST.get("filmname")
        film = FilmName(title=filmname)
        film.save()
        return redirect("index")

    return render(request, 'index.html',{"films":films})

def FilmDelete(request,id):
    film = FilmName.objects.get(id=id)
    film.delete()
    return redirect("index")