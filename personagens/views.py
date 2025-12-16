from rest_framework import generics
from .models import Personagens
from .serializer import PersonagensSerializer

class PersonagensListCreateView(generics.ListCreateAPIView):
    queryset = Personagens.objects.all()
    serializer_class = PersonagensSerializer

class PersonagemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Personagens.objects.all()
    serializer_class = PersonagensSerializer