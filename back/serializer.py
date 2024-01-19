from rest_framework import serializers
from .models import Mes

class MesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mes
        fields = '__all__'