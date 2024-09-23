from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
import os
from Netflix.movies.models import Movie


os.environ['DJANGO_SETTINGS_MODULE'] = 'Netflix.settings'
class MovieViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movie1 = Movie.objects.create(name='the witcher', genre='horror', imdb=9)
        self.movie2 = Movie.objects.create(name='bad boys', genre='comedy', imdb=9)
        self.movie3 = Movie.objects.create(name='half girlfriend', genre='romance', imdb=9)
        self.url = reverse('movie-actors')

    def test_list_movies(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['name'], 'the witcher')
        self.assertEqual(response.data[1]['name'], 'bad boys')
        self.assertEqual(response.data[2]['name'], 'half girlfriend')




# class TestGetCastedActors(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.actor = Actor.objects.create(name='Jamshid')
#         self.movie = Movie.objects.create(title='Jamshid')
#         self.movie.casted_actors.add(self.actor)

#     def test_get_casted_actors(self):
#         url = reverse('movie-detail', args=[self.movie.id])  # Use the correct URL name here
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('casted_actors', response.data)
#         self.assertEqual(response.data['casted_actors'][0]['name'], 'Jamshid')


# class TestMovieViewSet(TestCase):
#     def setUp(self) -> None:
#         self.movie = Movie.objects.create(name='Inception adda')
#         self.client = APIClient()

#
#     def test_order_by_imdb(self):
#         url = reverse('movie-list')
#         response = self.client.get(url, {'ordering': 'imdb'})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 0)
#         self.assertEqual(response.data[6]['name'], 'The Matrix')
        # self.assertEqual(response.data[1]['name'], 'Inception')
        # self.assertEqual(response.data[2]['name'], 'The Godfather')