from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from inventario.models import Proveedor, Categoria

# Lista de Proveedores
class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'proveedor_list.html'  # Nombre del template
    context_object_name = 'proveedores'   # Contexto para el template

# Crear un nuevo Proveedor
class ProveedorCreateView(CreateView):
    model = Proveedor
    fields = ['nombre', 'contacto', 'telefono', 'correo', 'direccion', 'categorias']
    template_name = 'proveedor_form.html'
    success_url = reverse_lazy('proveedor_list')  # Redirección tras éxito

# Actualizar un Proveedor existente
class ProveedorUpdateView(UpdateView):
    model = Proveedor
    fields = ['nombre', 'contacto', 'telefono', 'correo', 'direccion', 'categorias']
    template_name = 'proveedor_form.html'
    success_url = reverse_lazy('proveedor_list')

# Eliminar un Proveedor
class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = 'proveedor_confirm_delete.html'
    success_url = reverse_lazy('proveedor_list')

# Detalle de un Proveedor
class ProveedorDetailView(DetailView):
    model = Proveedor
    template_name = 'proveedor_detail.html'
    context_object_name = 'proveedor'
