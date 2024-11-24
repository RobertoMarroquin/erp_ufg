from django.db import models
from .vendedores import Vendedor


class RegistroHorario(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField(blank=True, null=True)  # Salida puede ser nula

    def __str__(self):
        return f"{self.vendedor} - {self.fecha}"
