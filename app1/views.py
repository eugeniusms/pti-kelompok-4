from django.shortcuts import render
from .forms import FilmForm, SFilmForm
from django.http import HttpRequest
from .models import SFilm
from serializers import SortSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class AddFilm(APIView):
    def post(self, request):
        film = SFilm.objects.create(
            judul = request.data['judul'] ,
            poster = request.data['poster'], 
            trailer = request.data['trailer'] ,
            genre = request.data['genre'],
            tahun_rilis = request.data['tahun_rilis'] ,
            likes = request.data['likes'] ,
            dislikes = request.data['dislikes']
        
        
        )
        serializers = SortSerializer(film, many = True)
        return Response(serializers.data, status= status.HTTP_201_CREATED)


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

def YearAscending(request):
    movie_sorted = SFilm.objects.all().order_by("tahun_rilis", "judul")
    context ={
        'movie_sorted' : movie_sorted
    }
    return render(request, 'app1/movie_sorted.html', context)

def YearDescending(request):
    movie_sorted = SFilm.objects.all().order_by("-tahun_rilis", "judul")
    context ={
        'movie_sorted' : movie_sorted
    }
    return render(request, 'app1/movie_sorted.html', context)

def LikesDescending(request):
    movie_sorted = SFilm.objects.all().order_by("genre", "-likes", "judul")
    context ={
        'movie_sorted' : movie_sorted
    }
    return render(request, 'app1/movie_sorted.html', context)