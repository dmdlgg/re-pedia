from rest_framework import serializers
from .models import Personagens

class PersonagensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personagens
        fields = '__all__'