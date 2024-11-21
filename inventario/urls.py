from django.urls import path, include  # Import include

from inventario.views import (    
    CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView, CategoriaDetailView,
    ProductoListView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView, ProductoDetailView,
    ProveedorListView, ProveedorCreateView, ProveedorUpdateView, ProveedorDeleteView, ProveedorDetailView,
    CompraListView, CompraCreateView, CompraUpdateView, CompraDeleteView, CompraDetailView,  # Compras
    DetalleCompraCreateView, DetalleCompraUpdateView, DetalleCompraDeleteView, # DetalleCompra
    TransaccionListView, TransaccionCreateView, TransaccionUpdateView, TransaccionDeleteView, TransaccionDetailView,  # Transacciones

)

app_name = 'inventario'  # Define the app_name

urlpatterns = [
    # Categorías URLs
    path('categorias/', CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/crear/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('categorias/<int:pk>/editar/', CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categorias/<int:pk>/eliminar/', CategoriaDeleteView.as_view(), name='categoria_delete'),
    path('categorias/<int:pk>/detalle/', CategoriaDetailView.as_view(), name='categoria_detail'),

    # Productos URLs
    path('productos/', ProductoListView.as_view(), name='producto_list'),
    path('productos/crear/', ProductoCreateView.as_view(), name='producto_create'),
    path('productos/<int:pk>/editar/', ProductoUpdateView.as_view(), name='producto_update'),
    path('productos/<int:pk>/', ProductoDetailView.as_view(), name='producto_detail'),
    path('productos/<int:pk>/eliminar/', ProductoDeleteView.as_view(), name='producto_delete'),

    # Proveedores URLs
    path('proveedores/', ProveedorListView.as_view(), name='proveedor_list'),
    path('proveedores/crear/', ProveedorCreateView.as_view(), name='proveedor_create'),
    path('proveedores/<int:pk>/editar/', ProveedorUpdateView.as_view(), name='proveedor_update'),
    path('proveedores/<int:pk>/eliminar/', ProveedorDeleteView.as_view(), name='proveedor_delete'),
    path('proveedores/<int:pk>/detalle/', ProveedorDetailView.as_view(), name='proveedor_detail'),


    # Compras URLs
    path('compras/', CompraListView.as_view(), name='compra_list'),
    path('compras/crear/', CompraCreateView.as_view(), name='compra_create'),
    path('compras/<int:pk>/editar/', CompraUpdateView.as_view(), name='compra_update'),
    path('compras/<int:pk>/', CompraDetailView.as_view(), name='compra_detail'),
    path('compras/<int:pk>/eliminar/', CompraDeleteView.as_view(), name='compra_delete'),

    # DetalleCompra URLs (nested within Compra)
    path('compra/<int:compra_pk>/detalle/create/', DetalleCompraCreateView.as_view(), name='detallecompra_create'),
    path('compra/detalle/<int:pk>/update/', DetalleCompraUpdateView.as_view(), name='detallecompra_update'),
    path('compra/detalle/<int:pk>/delete/', DetalleCompraDeleteView.as_view(), name='detallecompra_delete'),

    # Transacciones URLs (mostly automatic, but included for manual adjustments)
    path('transacciones/', TransaccionListView.as_view(), name='transaccion_list'),
    path('transacciones/crear/', TransaccionCreateView.as_view(), name='transaccion_create'),
    path('transacciones/<int:pk>/editar/', TransaccionUpdateView.as_view(), name='transaccion_update'),
    path('transacciones/<int:pk>/eliminar/', TransaccionDeleteView.as_view(), name='transaccion_delete'),
    path('transacciones/<int:pk>/', TransaccionDetailView.as_view(), name='transaccion_detail'),

]


