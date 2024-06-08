from django.db import models


class Pais(models.Model):
    codigoPais = models.CharField('Codigo Pais', max_length=10, unique=True)
    nombrePais = models.CharField('Nombre Pais', max_length=30, unique=True)
    descripcionPais = models.CharField(
        'Descripcion del Pais', max_length=30, unique=True)

    def __str__(self) -> str:
        return f'{self.codigoPais} - {self.nombrePais} - {self.descripcionPais}'
