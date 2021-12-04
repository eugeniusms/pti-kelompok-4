from django.shortcuts import render
from .forms import FilmForm, SFilmForm
from django.http import HttpRequest

# Create your views here.
def Film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():

            judul = request.POST.get('Judul Film ')
            genre = request.POST.get('Genre Film ')

            print(judul, genre)

    form = FilmForm()
    return render(request, 'form.html', {'form' : form})


def SFilm_detail(request):
    form = FilmForm()
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()

    form = SFilmForm()
    return render(request, 'form.html', {'form' : form})
