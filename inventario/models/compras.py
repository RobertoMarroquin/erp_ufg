from django.db import models
from .productos import Producto
from .transacciones import Transaccion


class Compra(models.Model):
    # Fecha de la compra
    fecha_compra = models.DateField()
    # Total de la compra
    total_compra = models.DecimalField(max_digits=10, decimal_places=2)
    # Provedor de Compra 
    proveedor = models.ForeignKey('Proveedor', on_delete=models.PROTECT, related_name='compras')

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"
        ordering = ['-fecha_compra']

    
    def __str__(self):
        # Representación en string del objeto Compra.  Usar f-strings para mejor legibilidad
        return f"Compra - {self.fecha_compra} - {self.total_compra}"  # Corregido: usar los nombres de campo correctos


class DetalleCompra(models.Model):
    # Relación con la Compra. Se eliminan los detalles si se elimina la compra.
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="detalles") # Agregar related_name
    # Relación con la Transacción asociada.
    transaccion = models.ForeignKey(Transaccion, on_delete=models.CASCADE, related_name="detalles_compra") # Agregar related_name y no es necesario usar string 'Transaccion'
    # Relación con el Producto. Se eliminan los detalles si se elimina el producto.
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="compras_detalle") # Agregar related_name
    # Cantidad de productos comprados.
    cantidad = models.PositiveIntegerField()
    # Precio unitario del producto al momento de la compra.
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    # Subtotal del detalle de la compra (cantidad * precio_unitario).
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        # Representación en string del objeto DetalleCompra. Usar f-strings
        return f"Detalle Compra - {self.compra} - {self.producto} - {self.cantidad}"

    def save(self, *args, **kwargs):
        # Calcular el subtotal automáticamente antes de guardar.
        self.subtotal = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)

#Signals para actualizar el total de la compra

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

@receiver(post_save, sender=DetalleCompra)
@receiver(post_delete, sender=DetalleCompra)
def actualizar_total_compra(sender, instance, **kwargs):
    """Actualiza el total de la compra después de guardar o eliminar un detalle."""

    total = 0
    for detalle in instance.compra.detalles.all(): #Usar related_name
        total += detalle.subtotal
    instance.compra.total_compra = total
    instance.compra.save()

