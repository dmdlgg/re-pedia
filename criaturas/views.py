from rest_framework import generics
from .models import Criaturas
from .serializer import CriaturasSerializer

class CriaturaListCreateView(generics.ListCreateAPIView):
    queryset = Criaturas.objects.all()
    serializer_class = CriaturasSerializer

class CriaturaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Criaturas.objects.all()
    serializer_class = CriaturasSerializer