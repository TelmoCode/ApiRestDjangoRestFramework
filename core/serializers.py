from rest_framework import serializers
from .models import Carro

class CarroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = ('id', 'marca', 'modelo' , 'ano')