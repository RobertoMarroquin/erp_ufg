from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from inventario.models import Producto, Categoria  # Asegúrate de importar Producto


# Lista de Productos
class ProductoListView(ListView):
    model = Producto
    template_name = 'producto_list.html'
    context_object_name = 'productos'


# Crear un nuevo Producto
class ProductoCreateView(CreateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'precio', 'categoria', 'proveedor', 'stock'] # Ajusta los campos según tu modelo
    template_name = 'producto_form.html'
    success_url = reverse_lazy('producto_list')  # Define el nombre de la URL para la lista


# Actualizar un Producto existente
class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'precio', 'categoria', 'proveedor', 'stock'] # Ajusta los campos según tu modelo
    template_name = 'producto_form.html'
    success_url = reverse_lazy('producto_list')


# Eliminar un Producto
class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'producto_confirm_delete.html'
    success_url = reverse_lazy('producto_list')


# Detalle de un Producto
class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'producto_detail.html'
    context_object_name = 'producto'

