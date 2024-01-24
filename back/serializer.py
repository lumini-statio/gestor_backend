from rest_framework import serializers
from .models import Mes, Gasto

class MesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mes
        fields = '__all__'


class GastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasto
        fields = '__all__'