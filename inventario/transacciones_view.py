from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from inventario.models import Transaccion

# Lista de Transacciones
class TransaccionListView(ListView):
    model = Transaccion
    template_name = 'transaccion_list.html'
    context_object_name = 'transacciones'

# Crear una nueva Transacción
class TransaccionCreateView(CreateView):
    model = Transaccion
    fields = ['tipo', 'monto', 'fecha', 'descripcion']
    template_name = 'transaccion_form.html'
    success_url = reverse_lazy('transaccion_list')

# Actualizar una Transacción
class TransaccionUpdateView(UpdateView):
    model = Transaccion
    fields = ['tipo', 'monto', 'fecha', 'descripcion']
    template_name = 'transaccion_form.html'
    success_url = reverse_lazy('transaccion_list')

# Eliminar una Transacción
class TransaccionDeleteView(DeleteView):
    model = Transaccion
    template_name = 'transaccion_confirm_delete.html'
    success_url = reverse_lazy('transaccion_list')

# Detalle de una Transacción
class TransaccionDetailView(DetailView):
    model = Transaccion
    template_name = 'transaccion_detail.html'
    context_object_name = 'transaccion'
