from django.contrib import admin
from . import models


@admin.register(models.MovieType)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Movies)
class moviesAdmin(admin.ModelAdmin):
    """ Custom User Admin """
    list_display = ("id", "title_kor")
