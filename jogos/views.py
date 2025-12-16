from rest_framework import generics
from .models import Jogos
from .serializer import JogosSerializer

class JogosListCreateView(generics.ListCreateAPIView):
    queryset = Jogos.objects.all()
    serializer_class = JogosSerializer

class JogosRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jogos.objects.all()
    serializer_class = JogosSerializer