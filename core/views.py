from .serializers import CarroSerializers
from django.shortcuts import render
from rest_framework import viewsets
from .models import Carro

class CarroViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializers 
