from django.contrib import admin
from personal.models import Vendedor, RegistroHorario, PermisoLaboral


class RegistroHorarioInline(admin.TabularInline):
    model = RegistroHorario
    extra = 1
    autocomplete_fields = ['vendedor']  # Autocomplete for vendedor
    #fields = ['vendedor', 'fecha', 'hora_entrada', 'hora_salida']


class PermisoLaboralInline(admin.TabularInline):
    model = PermisoLaboral
    extra = 1


@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ('user', 'numero_caja')  # Fields to display
    search_fields = ('user__first_name', 'user__last_name', 'user__username','numero_caja') # Search by user fields and numero_caja
    # No filters needed here likely, as you would filter by user properties in UserAdmin
    inlines = [RegistroHorarioInline, PermisoLaboralInline]  # Inline editing for related models
    #autocomplete_fields = ['user']




@admin.register(RegistroHorario)
class RegistroHorarioAdmin(admin.ModelAdmin):
    list_display = ('vendedor', 'fecha', 'hora_entrada', 'hora_salida')
    search_fields = ('vendedor__user__first_name', 'vendedor__user__last_name', 'fecha')
    list_filter = ('vendedor', 'fecha') # Filter by vendedor and fecha
    autocomplete_fields = ['vendedor'] #Autocomplete for Vendedor


@admin.register(PermisoLaboral)
class PermisoLaboralAdmin(admin.ModelAdmin):
    list_display = ('vendedor', 'fecha_inicio', 'fecha_fin', 'motivo', 'duracion_horas')
    search_fields = ('vendedor__user__first_name', 'vendedor__user__last_name', 'motivo') # Buscar por nombre, apellido y motivo
    list_filter = ('vendedor', 'fecha_inicio', 'fecha_fin')
    autocomplete_fields = ['vendedor'] #Autocomplete for Vendedor



