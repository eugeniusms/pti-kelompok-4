from django.shortcuts import render
from .forms import FilmForm, SFilmForm, FilmAja
from django.http import HttpRequest
from .models import SFilm

# Create your views here.
def AddFilm(request):
    if request.method == 'POST':
        print("MASUK KE SINI")
        form = FilmAja(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():

            print("FORMNYA VALID")
            form.save()
            
    form = FilmAja()
    return render(request, 'app1/form.html', {'form' : form})


def SFilm_detail(request):
    form = FilmForm()
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()

    form = SFilmForm()
    return render(request, 'form.html', {'form' : form})

def Movies(request):
    movie_list = SFilm.objects.all()
    context = {
        'movie_list' : movie_list
    }
    return render(request, 'app1/movies.html',  context)
