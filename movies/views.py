from django.db.migrations import serializer
from rest_framework import serializers, filters
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from .models import Movie, Actor, Comment  # Replace with the path to your models.py
from .serializers import MovieSerializer, ActorSerializer, \
    CommentSerializer  # Replace with the path to your serializers.py


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    order_fields = ['imdb', '-imdb']
    search_fields = ['name','genre']


    @action(methods=['POST', 'GET'], detail=True, url_path='add-actor')
    def add_actor(self, request, pk=None):
        movie = self.get_object()

        if request.method == 'POST':
            actor_id = request.data.get('actor_id')

            movie.casted_actors.add(actor_id)
            movie.save()

            serializer = MovieSerializer(movie)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if request.method == 'GET':
            casted_actors = movie.casted_actors.all()
            serializer = ActorSerializer(casted_actors, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['DELETE'], detail=True, url_path='remove-actor')
    def remove_actor(self, request, pk=None):
        movie = self.get_object()
        actor_id = request.data.get('actor_id')
        movie.casted_actors.remove(actor_id)
        movie.save()

        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    @action(methods=['POST'], detail=False, url_path='create-actor')
    def create_actor(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()


class CommentAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        comments = Comment.objects.filter(user_id=request.user)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        comment = Comment.objects.get(id=id)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieActorAPIView(APIView):
    def get(self, request, id):
        movie = get_object_or_404(Movie, pk=id)
        actors = movie.casted_actors.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
