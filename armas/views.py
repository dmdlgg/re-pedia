from rest_framework import generics
from .models import Armas
from .serializer import ArmasSerializer

class ArmaListCreateView(generics.ListCreateAPIView):
    queryset = Armas.objects.all()
    serializer_class = ArmasSerializer

class ArmaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Armas.objects.all()
    serializer_class = ArmasSerializer
