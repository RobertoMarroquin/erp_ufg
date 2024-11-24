from django.db import models
from .vendedores import Vendedor

class PermisoLaboral(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    fecha_inicio = models.DateField() #Fecha en que inicia el permiso
    fecha_fin = models.DateField(blank=True, null=True)  # Permiso puede no tener fecha de fin aún
    motivo = models.TextField()
    duracion_horas = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True) # Duración en horas (opcional)

    def __str__(self):
        return f"{self.vendedor} - {self.fecha_inicio}: {self.motivo}"
