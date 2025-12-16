from django.urls import path
from . import views

urlpatterns = [

    path('criaturas/', views.CriaturaListCreateView.as_view(), name='criaturas'),
    path('criaturas/<int:pk>', views.CriaturaRetrieveUpdateDestroyView.as_view(), name='criatura-unity'),

]
