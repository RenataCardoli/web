from unicodedata import name
from django.db import models


class Registro (models.Model):
    name = models.CharField(max_length=30)
    edad = models.IntegerField()
    dni = models.IntegerField()
    email = models.CharField(max_length=30)