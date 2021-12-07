from django.shortcuts import render
from .forms import FilmForm, SFilmForm
from django.http import HttpRequest
from .models import SFilm
from .serializers import SortSerializer
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
        print("hallo")
        movie_sorted = SFilm.objects.all().order_by("-tahun_rilis", "judul")
        print("dibawah get")
        serializers = SortSerializer(movie_sorted, many = True)
        print(serializers)
        return Response(serializers.data)
    
# Tambahin punya Jere tapi belum ke serializer
class SearchResultsView(request):
    def get(self,request):
        query = request.GET.get('q')
        searched_movies = SFilm.objects.filter(judul__icontains=query)
        serializers = # wait
        context = {
            'searched_movies': searched_movies
        }
        template_name = 'app1/search_results.html'

        return render(request, template_name, context) 
