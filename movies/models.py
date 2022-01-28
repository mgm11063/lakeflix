from core import models as core_models
from django.db import models
from django.urls import reverse


class AbstractItem(core_models.TimeStampedModel):
    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class MovieType(AbstractItem):

    pass


class Movies(models.Model):
    """ Movies Model """
    class Meta:
        db_table = "movie"

    title_kor = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    play_time = models.CharField(max_length=20)
    director = models.CharField(max_length=200)
    justwatch_rating = models.CharField(max_length=10)
    imdb_rating = models.CharField(max_length=10)
    synopsis = models.TextField(max_length=500)
    poster = models.CharField(max_length=100)
    genre = models.ManyToManyField(MovieType, blank=True)

    def __str__(self):
        return self.title_kor

    def get_absolute_url(self):
        return reverse("movies:detail", kwargs={'pk': self.pk})
