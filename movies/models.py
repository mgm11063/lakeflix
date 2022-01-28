from django.db import models


class Movies(models.Model):
    """ Movies Model """
    class Meta:
        db_table = "movie"

    title_kor = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    genre = models.CharField(max_length=200)
    play_time = models.CharField(max_length=20)
    director = models.CharField(max_length=200)
    justwatch_rating = models.CharField(max_length=10)
    imdb_rating = models.CharField(max_length=10)
    synopsis = models.TextField(max_length=500)
    poster = models.CharField(max_length=100)
