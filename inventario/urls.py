from django.urls import path
from inventario.views import (
    CategoriaListView,
    CategoriaCreateView,
    CategoriaUpdateView,
    CategoriaDeleteView,
    CategoriaDetailView,
    #ProductoCreateView,
    #ProductoUpdateView,
    #ProductoDeleteView,
    #ProductoDetailView,
    #TransaccionCreateView,
    #TransaccionUpdateView,
    #TransaccionDeleteView,
    #TransaccionDetailView,
    #CompraCreateView,
    #CompraUpdateView,
    #CompraDeleteView,
    #CompraDetailView,
    #ProveedorCreateView,
    #ProveedorUpdateView,
    #ProveedorDeleteView,
    #ProveedorDetailView,
)



urlpatterns = [
    path('categorias/', CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/crear/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('categorias/<int:pk>/editar/', CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categorias/<int:pk>/eliminar/', CategoriaDeleteView.as_view(), name='categoria_delete'),
    path('categorias/<int:pk>/detalle/', CategoriaDetailView.as_view(), name='categoria_detail'),
]

