from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    contacto = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(blank=True)
    direccion = models.TextField(blank=True)
    categorias = models.ManyToManyField('Categoria', related_name='proveedores')  # Relación muchos a muchos con categorias

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ['nombre']
        
