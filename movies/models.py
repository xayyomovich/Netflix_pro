from django.db import models
from django.contrib.auth.models import User


class Actor(models.Model):
    # objects = None
    name = models.CharField(max_length=200)
    birthday = models.DateField()
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    imdb = models.IntegerField()
    genre = models.CharField(max_length=200)
    casted_actors = models.ManyToManyField(Actor, related_name='movies')

    def __str__(self):
        return self.name


class Comment(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateField()


class Cast(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    role = models.CharField(max_length=200, blank=True)
