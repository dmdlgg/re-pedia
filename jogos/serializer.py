from rest_framework import serializers
from .models import Jogos

class JogosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogos
        fields = '__all__'