from datetime import datetime
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ValidationError
from .models import Movie, Actor, Comment


class ActorSerializer(serializers.ModelSerializer):
    # birthday = serializers.DateField()


    class Meta:
        model = Actor
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    casted_actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('name', 'year', 'imdb', 'genre', 'casted_actors')
        # fields = '__all__'


def validate_birthday(value):
    if value < datetime.date(year=1950, month=1, day=1):
        raise ValidationError("Birthday cannot be less than January 1st, 1950.")
    return value


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
