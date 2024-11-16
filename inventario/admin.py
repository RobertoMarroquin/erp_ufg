from django.contrib import admin
from .models import Categoria, Producto, Transaccion, Compra, DetalleCompra, Proveedor


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 
                    'descripcion', 
                    'precio', 
                    'porcentaje_ganancia', 
                    'creado_en',
                    'actualizado_en',
                    'fecha_vencimiento',
                    'stock',
                    'categoria')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('categoria',)
    autocomplete_fields = ('categoria',)


@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'producto', 'cantidad', 'fecha', 'creado_en', 'modificado_en')
    list_filter = ('tipo', 'producto', 'fecha')
    search_fields = ('producto__nombre',)
    autocomplete_fields = ('producto',)


class DetalleCompraInline(admin.TabularInline):
    model = DetalleCompra
    extra = 1
    max_num = 10
    fields = ('producto',"cantidad","precio_unitario","subtotal")
    readonly_fields = ('precio_unitario','subtotal',)
    can_delete = True


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = [DetalleCompraInline]
    list_display = ("id",'proveedor','fecha_compra', 'total_compra')
    search_fields = ('fecha_compra',"proveedor__nombre")
    autocomplete_fields = ["proveedor"]
    readonly_fields = ('total_compra',)



@admin.register(DetalleCompra)
class DetalleCompraAdmin(admin.ModelAdmin):
    # Define fields to display, search, filter, etc. as needed
    pass # Placeholder until fields are defined


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    # Define fields to display, search, filter, etc. as needed
    pass # Placeholder until fields are defined

