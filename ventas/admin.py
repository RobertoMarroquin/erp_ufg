from django.contrib import admin
from ventas.models import Cliente, Factura, DetalleFactura
from inventario.models import Producto  # Import Producto for autocomplete

class DetalleFacturaInline(admin.TabularInline):
    model = DetalleFactura
    extra = 1
    autocomplete_fields = ['producto']  # Autocomplete for producto


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'dui', 'nit')
    search_fields = ('nombre', 'email', 'telefono', 'dui', 'nit')  # All fields searchable
    list_filter = ('nombre', 'email')  # Filter by nombre and email


@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'fecha_emision', 'total')
    inlines = [DetalleFacturaInline]
    search_fields = ('cliente__nombre', 'id')  # Search by related cliente nombre and id
    list_filter = ('fecha_emision', 'cliente')  # Filter by fecha and cliente
    autocomplete_fields = ['cliente'] #Autocomplete for Cliente


@admin.register(DetalleFactura)
class DetalleFacturaAdmin(admin.ModelAdmin):
    list_display = ('factura', 'producto', 'cantidad', 'precio_venta')
    search_fields = ('factura__cliente__nombre', 'producto__nombre') # Search by related fields
    list_filter = ('producto', 'factura__cliente') #Filtrar por producto y cliente de factura
    autocomplete_fields = ['producto','factura'] #Autocomplete for Producto and Factura



