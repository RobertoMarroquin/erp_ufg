from django.db import models
from .productos import Producto

class Transaccion(models.Model):
    TIPO_CHOICES = [
        ('Entrada', 'Entrada'),
        ('Salida', 'Salida'),
    ]

    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateField()
    creado_en = models.DateTimeField(auto_now_add=True)
    modificado_en = models.DateTimeField(auto_now=True)
    # Agregar campo para almacenar la referencia de la compra o venta
    referencia_compra = models.CharField(max_length=255, blank=True, null=True)
    referencia_venta = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"{self.tipo} - {self.producto.nombre} - {self.cantidad}"
    class Meta:
        verbose_name = "Transacción"
        verbose_name_plural = "Transacciones"
        ordering = ['-fecha', 'tipo']

    # Agregar método para actualizar el stock del producto después de una transacción
    def actualizar_stock_producto(self):
        producto = self.producto
        if self.tipo == 'Entrada':
            producto.stock += self.cantidad
        elif self.tipo == 'Salida':
            producto.stock -= self.cantidad
        producto.save()
    # Método para guardar la transacción y actualizar el stock del producto
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.actualizar_stock_producto()
    
    #Se agrega un metodo para obtener el stock del producto despues de la transaccion
    def get_stock_after_transaction(self):
        producto = self.producto
        stock_inicial = producto.stock
        if self.tipo == 'Entrada':
            return stock_inicial + self.cantidad
        elif self.tipo == 'Salida':
            return stock_inicial - self.cantidad
        return stock_inicial
