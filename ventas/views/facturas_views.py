from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.forms import inlineformset_factory
from ventas.models import Factura, DetalleFactura, Cliente
from inventario.models import Producto

#Para trabajar con formsets, simplifica la creación de formularios para modelos relacionados,
#como es el caso de DetalleFactura con Factura.

class FacturaListView(ListView):
    model = Factura
    template_name = 'factura_list.html'
    context_object_name = 'facturas'

class FacturaCreateView(CreateView):
    model = Factura
    template_name = 'factura_form.html'
    fields = ['cliente'] #Solo cliente inicialmente, detalles se agregan después.
    success_url = reverse_lazy('ventas:factura_list')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['detalle_facturas'] = DetalleFacturaFormSet(self.request.POST)
        else:
            context['detalle_facturas'] = DetalleFacturaFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        detalle_facturas = context['detalle_facturas']
        if detalle_facturas.is_valid():
            self.object = form.save()
            detalle_facturas.instance = self.object
            detalle_facturas.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form)) #Re-render


class FacturaUpdateView(UpdateView):
    model = Factura
    template_name = 'factura_form.html'
    fields = ['cliente']
    success_url = reverse_lazy('ventas:factura_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['detalle_facturas'] = DetalleFacturaFormSet(self.request.POST, instance=self.object)
        else:
            context['detalle_facturas'] = DetalleFacturaFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        detalle_facturas = context['detalle_facturas']
        if detalle_facturas.is_valid():
            self.object = form.save()
            detalle_facturas.instance = self.object
            detalle_facturas.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class FacturaDeleteView(DeleteView):
    model = Factura
    template_name = 'factura_confirm_delete.html'
    success_url = reverse_lazy('ventas:factura_list')



class FacturaDetailView(DetailView):
    model = Factura
    template_name = 'factura_detail.html'
    context_object_name = 'factura'



# Formset para DetalleFactura, formulario en línea para crear/editar varios
# detalles de factura a la vez.

DetalleFacturaFormSet = inlineformset_factory(
    Factura,
    DetalleFactura,
    fields=['producto', 'cantidad', 'precio_venta'],
    extra=1, #Permitir agregar un detalle extra en el formulario
    can_delete=True, #Permitir eliminar detalles existentes
)



