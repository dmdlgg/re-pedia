from django.urls import path
from . import views

urlpatterns = [

    path('armas/', views.ArmaListCreateView.as_view(), name='armas'),
    path('armas/<int:pk>', views.ArmaRetrieveUpdateDestroyView.as_view(), name='arma-unity'),

]
