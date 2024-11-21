from django.db import models
from .categorias_productos  import Categoria
from .proovedores import Proveedor



# Modelo para representar un producto en el inventario.
class Producto(models.Model):
    # Nombre del producto.
    nombre = models.CharField(max_length=255)
    # Descripción detallada del producto.
    descripcion = models.TextField()
    # Precio de costo del producto.
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    # Porcentaje de ganancia deseado para el producto.
    porcentaje_ganancia = models.DecimalField(max_digits=5, decimal_places=2)
    # Fecha y hora de creación del registro del producto.
    creado_en = models.DateTimeField(auto_now_add=True)
    # Fecha y hora de la última actualización del registro del producto.
    actualizado_en = models.DateTimeField(auto_now=True)
    # Fecha de vencimiento del producto (opcional).
    fecha_vencimiento = models.DateField(blank=True, null=True)
    # Stock inicial del producto.
    stock = models.IntegerField()
    # Categoría a la que pertenece el producto.
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    # Proovedor de producto, se sete en null al eliminar al proveedor para no tener perdidas de productos accidentalmente
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, blank=True, related_name='productos')


    # Representación en string del objeto Producto.
    def __str__(self):
        return self.nombre

    # Metadatos del modelo Producto.
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Producto"
        ordering = ['nombre']

    # Método para calcular el precio de venta del producto.
    def precio_venta(self):
        """Calcula el precio de venta del producto."""
        return self.precio * (1 + self.porcentaje_ganancia / 100)

    # Método para calcular el stock actual del producto considerando las transacciones.
    #def stock_actual(self):  #Este método parece redundante. Se calcula el stock en el modelo Transaccion
    #    """Calcula el stock actual del producto considerando las transacciones."""
    #    entradas = Transaccion.objects.filter(producto=self, tipo='Entrada').aggregate(total=models.Sum('cantidad'))['total'] or 0
    #    salidas = Transaccion.objects.filter(producto=self, tipo='Salida').aggregate(total=models.Sum('cantidad'))['total'] or 0
    #    return self.stock + entradas - salidas
#
    # Método para actualizar el stock del producto según el tipo de transacción.
    #def actualizar_stock(self, cantidad, tipo): #Este método es redundante. Se actualiza el stock en el modelo Transaccion.
    #    """Actualiza el stock del producto según el tipo de transacción."""
    #    if tipo == 'Entrada':
    #        self.stock += cantidad
    #    elif tipo == 'Salida':
    #        self.stock -= cantidad
    #    self.save()

