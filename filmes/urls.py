from django.urls import path
from . import views

urlpatterns = [

    path('filmes/', views.FilmesListCreateView.as_view(), name='filmes'),
    path('filmes/<int:pk>', views.FilmeRetrieveUpdateDestroyView.as_view(), name='filme-unity'),

]
