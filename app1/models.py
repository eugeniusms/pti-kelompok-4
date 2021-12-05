from django.db import models

# Create your models here.
class SFilm(models.Model):
    judul = models.CharField(max_length=100)
    poster = models.ImageField(upload_to="images")
    trailer = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    tahun_rilis = models.IntegerField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.judul

# class Movie(models.Model):
#     judul = models.CharField(max_length=100)
#     poster = models.CharField(max_length=100)
#     trailer = models.CharField(max_length=100)
#     genre = models.CharField(max_length=100)
#     tahun_rilis = models.DateTimeField()

#     def __str__(self):
#         return self.judulss