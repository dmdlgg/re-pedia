from rest_framework import serializers
from .models import Armas

class ArmasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Armas
        fields = '__all__'