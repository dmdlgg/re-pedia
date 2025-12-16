from django.urls import path
from . import views

urlpatterns = [

    path('jogos/', views.JogosListCreateView.as_view(), name='jogos'),
    path('jogos/<int:pk>', views.JogosRetrieveUpdateDestroyView.as_view(), name='jogo-unity'),

]