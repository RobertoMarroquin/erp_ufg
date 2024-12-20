from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True) 
    dui = models.CharField(max_length=20, blank=True, null=True)
    nit = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nombre