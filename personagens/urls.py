from django.urls import path
from . import views

urlpatterns = [

    path('personagens/', views.PersonagensListCreateView.as_view(), name='personagens'),
    path('personagens/<int:pk>', views.PersonagemRetrieveUpdateDestroyView.as_view(), name='personagem-unity'),

]