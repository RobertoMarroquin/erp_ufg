from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
<<<<<<< HEAD
from inventario.models import Categoria
=======
from .models import Categoria
>>>>>>> 9fb6699 (creacion de vistas para modelo de productos)

# Lista de Categorías
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria_list.html'  # Cambiar por el nombre del template
    context_object_name = 'categorias'     # Nombre del contexto a usar en el template

# Crear una nueva Categoría
class CategoriaCreateView(CreateView):
    model = Categoria
    fields = ['nombre', 'descripcion']  # Campos que se mostrarán en el formulario
    template_name = 'categoria_form.html'
    success_url = reverse_lazy('categoria_list')  # Redirección tras éxito

# Actualizar Categoría existente
class CategoriaUpdateView(UpdateView):
    model = Categoria
    fields = ['nombre', 'descripcion']
    template_name = 'categoria_form.html'
    success_url = reverse_lazy('categoria_list')

# Eliminar una Categoría
class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'categoria_confirm_delete.html'
    success_url = reverse_lazy('categoria_list')

# Detalle de una Categoría
class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'categoria_detail.html'
    context_object_name = 'categoria'
