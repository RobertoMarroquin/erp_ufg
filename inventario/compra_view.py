from django.db import models
from django.utils import timezone
from .models import Proveedor  # Suponiendo que ya existe el modelo Proveedor

class Compra(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name="compras")
    fecha = models.DateTimeField(default=timezone.now)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"Compra de {self.proveedor.nombre} - {self.total}"

    class Meta:
        ordering = ['-fecha']
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Compra

# Listar Compras
class CompraListView(ListView):
    model = Compra
    template_name = 'compra_list.html'
    context_object_name = 'compras'

# Crear Compra
class CompraCreateView(CreateView):
    model = Compra
    fields = ['proveedor', 'fecha', 'total', 'descripcion']
    template_name = 'compra_form.html'
    success_url = reverse_lazy('compra_list')

# Actualizar Compra
class CompraUpdateView(UpdateView):
    model = Compra
    fields = ['proveedor', 'fecha', 'total', 'descripcion']
    template_name = 'compra_form.html'
    success_url = reverse_lazy('compra_list')

# Detalle de Compra
class CompraDetailView(DetailView):
    model = Compra
    template_name = 'compra_detail.html'
    context_object_name = 'compra'

# Eliminar Compra
class CompraDeleteView(DeleteView):
    model = Compra
    template_name = 'compra_confirm_delete.html'
    success_url = reverse_lazy('compra_list')
