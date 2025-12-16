from rest_framework import generics
from .models import Series
from .serializer import SeriesSerializer

class SeriesListCreateView(generics.ListCreateAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer

class SerieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer