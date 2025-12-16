from rest_framework import serializers
from .models import Criaturas

class CriaturasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criaturas
        fields = '__all__'