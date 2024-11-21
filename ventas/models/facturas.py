from django.db import models
from inventario.models import Producto 
from .clientes import Cliente 



class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_emision = models.DateField(auto_now_add=True)  # Fecha de creación automática
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) #Almacenar el total

    def __str__(self):
        return f"Factura N° {self.id} - Cliente: {self.cliente.nombre}"

    def calcular_total(self):
        detalles = self.detallefactura_set.all() # Asegúrate que el nombre del related_name es correcto
        total = sum(detalle.cantidad * detalle.precio_venta for detalle in detalles)
        self.total = total
        self.save()
        

class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en Factura {self.factura.id}"
       

# Signals para actualizar el total de la factura al guardar un DetalleFactura
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=DetalleFactura)
def actualizar_total_factura(sender, instance, created, **kwargs):
    instance.factura.calcular_total() # Llama al método de la factura para recalcular
