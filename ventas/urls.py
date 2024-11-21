from django.urls import path
from . import views

app_name = 'ventas'

urlpatterns = [
    # Cliente URLs
    path('clientes/', views.ClienteListView.as_view(), name='cliente_list'),
    path('clientes/crear/', views.ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/<int:pk>/eliminar/', views.ClienteDeleteView.as_view(), name='cliente_delete'),
    path('clientes/<int:pk>/detalle/', views.ClienteDetailView.as_view(), name='cliente_detail'),

    # Factura URLs
    path('facturas/', views.FacturaListView.as_view(), name='factura_list'),
    path('facturas/crear/', views.FacturaCreateView.as_view(), name='factura_create'),
    path('facturas/<int:pk>/editar/', views.FacturaUpdateView.as_view(), name='factura_update'),
    path('facturas/<int:pk>/eliminar/', views.FacturaDeleteView.as_view(), name='factura_delete'),
    path('facturas/<int:pk>/detalle/', views.FacturaDetailView.as_view(), name='factura_detail'),
]
