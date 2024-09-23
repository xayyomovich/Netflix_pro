from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import MovieViewSet, ActorViewSet, CommentAPIView
from rest_framework.routers import DefaultRouter
from .views import MovieActorAPIView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

router = DefaultRouter()
router.register('movies', MovieViewSet)
router.register('actors', ActorViewSet)
# router.register('comments', CommentAPIView, 'comments')


schema_view = get_schema_view(
    openapi.Info(
        title='Movie application',
        default_version='v1',
        description='Swagger dock for rest API',
        contact=openapi.Contact(email='jamolov@gmail.com')
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('', include(router.urls)),
    path('movies/<int:id>/actors/', MovieActorAPIView.as_view(), name='movie-actors'),
    path('auth/', obtain_auth_token),
    path('comments/', CommentAPIView.as_view(), name='comments'),
    path('comments/<int:id>/', CommentAPIView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui')
]






from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
# from Netflix.movies.models import Movie

class MovieViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movie1 = Movie.objects.create(name='the witcher', genre='horror', imdb=9)
        self.movie2 = Movie.objects.create(name='bad boys', genre='comedy', imdb=9)
        self.movie3 = Movie.objects.create(name='half girlfriend', genre='romance', imdb=9)

        self.url = reverse('movie-actors', kwargs={'id': self.movie1.id})

    def test_list_movies(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 3)

        movie_names = [movie['name'] for movie in response.data]
        self.assertIn('the witcher', movie_names)
        self.assertIn('bad boys', movie_names)
        self.assertIn('half girlfriend', movie_names)



















# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('movies/', MovieAPIView.as_view()),
#     path('actors/', ActorAPIView.as_view())
# ]
