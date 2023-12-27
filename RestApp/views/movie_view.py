from rest_framework import viewsets
from RestApp.models import Movie
from RestApp.serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']