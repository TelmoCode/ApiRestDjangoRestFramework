from django.db import models
from django.db.models.fields import CharField

class Carro(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()

    def __str__(self):
        return self.marca

