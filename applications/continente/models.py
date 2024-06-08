from django.db import models


class Continente(models.Model):
    nombre_continente = models.CharField(
        'Nombre continente', max_length=20, unique=True)
