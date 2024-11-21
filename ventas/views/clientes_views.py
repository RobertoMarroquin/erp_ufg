from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from ventas.models import Cliente

class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente_list.html'  # Crea este template
    context_object_name = 'clientes'


class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'cliente_form.html'  # Crea este template
    fields = ['nombre', 'email', 'telefono', 'direccion', 'dui', 'nit'] # Campos de tu modelo
    success_url = reverse_lazy('ventas:cliente_list') # Usa 'ventas:nombre_de_ruta'


class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'cliente_form.html'  # Puedes usar el mismo template que CreateView
    fields = ['nombre', 'email', 'telefono', 'direccion', 'dui', 'nit']
    success_url = reverse_lazy('ventas:cliente_list')


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente_confirm_delete.html'  # Crea este template
    success_url = reverse_lazy('ventas:cliente_list')


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente_detail.html'  # Crea este template
    context_object_name = 'cliente'

