

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Producto

# Listar productos
class ProductoListView(ListView):
    model = Producto
    template_name = 'producto_list.html'  # Plantilla HTML para mostrar los productos
    context_object_name = 'productos'  # Nombre del contexto para usar en la plantilla

# Crear un nuevo producto
class ProductoCreateView(CreateView):
    model = Producto
    template_name = 'producto_form.html'  # Plantilla para el formulario
    fields = ['nombre', 'descripcion', 'precio', 'stock']  # Campos que se mostrarán en el formulario
    success_url = reverse_lazy('producto-list')  # Redirigir al listado tras la creación

# Actualizar un producto existente
class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = 'producto_form.html'  # Usa la misma plantilla del formulario
    fields = ['nombre', 'descripcion', 'precio', 'stock']
    success_url = reverse_lazy('producto-list')

# Eliminar un producto
class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'producto_confirm_delete.html'  # Plantilla para confirmar la eliminación
    success_url = reverse_lazy('producto-list')

# Detalles de un producto
class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'producto_detail.html'  # Plantilla para mostrar los detalles
    context_object_name = 'producto'  # Nombre del contexto para usar en la plantilla
