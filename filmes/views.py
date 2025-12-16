from rest_framework import generics
from .models import Filmes
from .serializer import FilmesSerializer

class FilmesListCreateView(generics.ListCreateAPIView):
    queryset = Filmes.objects.all()
    serializer_class = FilmesSerializer

class FilmeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Filmes.objects.all()
    serializer_class = Filmes
