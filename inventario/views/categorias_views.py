from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from inventario.models import Categoria

# Lista de Categorías
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'inventario/categorias/CategoriaListViewTemplate.html'  # Nombre completo de la plantilla
    context_object_name = 'categorias'

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
