from django.shortcuts import render
from .forms import FilmForm, SFilmForm
from django.http import HttpRequest
from .models import SFilm
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SortSerializer
from rest_framework import serializers, status

# Create your views here.
def AddFilm(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():

            judul = request.POST.get('Judul Film ')
            genre = request.POST.get('Genre Film ')

            print(judul, genre)

    form = FilmForm()
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

class YearAscending(APIView):
    def get(self,request):
        movie_sorted = SFilm.objects.all().order_by("tahun_rilis", "judul")
        serializers = SortSerializer(movie_sorted, many = True)
        return Response(serializers.data)

class YearDescending(APIView):
    def get(self,request):
        movie_sorted = SFilm.objects.all().order_by("-tahun_rilis", "judul")
        serializers = SortSerializer(movie_sorted, many = True)
        return Response(serializers.data)

class LikesDescending(APIView):
    def get(self,request):
        movie_sorted = SFilm.objects.all().order_by("genre", "-likes", "judul")
        serializers = SortSerializer(movie_sorted, many = True)
        return Response(serializers.data)
