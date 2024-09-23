from django.contrib import admin
from .models import Movie, Actor, Cast, Comment

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'imdb', 'genre')


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday', 'gender')



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('movie_id', 'text', 'created_date')

@admin.register(Cast)
class CastAdmin(admin.ModelAdmin):
    list_display = ('movie', 'actor', 'role')


