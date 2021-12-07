from .models import SFilm
from rest_framework import serializers

class SortSerializer(serializers.ModelSerializer):
    class Meta:
        model = SFilm
        fields = [ 'judul' , 'poster', 'trailer' ,'genre','tahun_rilis' ,'likes' ,'dislikes']
