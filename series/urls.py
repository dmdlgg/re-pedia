from django.urls import path
from . import views

urlpatterns = [

    path('series/', views.SeriesListCreateView.as_view(), name='series'),
    path('series/<int:pk>', views.SerieRetrieveUpdateDestroyView.as_view(), name='serie-unity'),

]