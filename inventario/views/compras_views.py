from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from inventario.models import Compra, DetalleCompra, Producto, Proveedor, Transaccion
from inventario.forms import CompraForm, DetalleCompraFormSet


class CompraListView(ListView):
    model = Compra
    template_name = 'compra_list.html'
    context_object_name = 'compras'


class CompraCreateView(CreateView):
    model = Compra
    fields = ['fecha_compra', 'proveedor']
    template_name = 'compra_form.html'
    success_url = reverse_lazy('compra_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['detalle_formset'] = DetalleCompraFormSet(self.request.POST)
        else:
            context['detalle_formset'] = DetalleCompraFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        detalle_formset = context['detalle_formset']
        if detalle_formset.is_valid():
            self.object = form.save() # save the compra object
            detalle_formset.instance = self.object
            detalle_formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))



class CompraUpdateView(UpdateView):
    model = Compra
    fields = ['fecha_compra', 'proveedor']
    template_name = 'compra_form.html'
    success_url = reverse_lazy('compra_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['detalle_formset'] = DetalleCompraFormSet(self.request.POST)
        else:
            context['detalle_formset'] = DetalleCompraFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        detalle_formset = context['detalle_formset']
        if detalle_formset.is_valid():
            self.object = form.save() # save the compra object
            detalle_formset.instance = self.object
            detalle_formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))




class CompraDeleteView(DeleteView):
    model = Compra
    template_name = 'compra_confirm_delete.html'
    success_url = reverse_lazy('compra_list')



#Detalles de Compra Views
class CompraDetailView(DetailView):
    model = Compra
    template_name = 'compra_detail.html'
    context_object_name = 'compra'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detalles'] = DetalleCompra.objects.filter(compra=self.object)
        return context


class DetalleCompraCreateView(CreateView):
    model = DetalleCompra
    fields = ['producto', 'cantidad', 'precio_unitario']
    template_name = 'detallecompra_form.html'

    def get_success_url(self):
        return reverse_lazy('compra_detail', kwargs={'pk': self.kwargs['compra_pk']})


    def form_valid(self, form):
        detalle_compra = form.save(commit=False)
        compra = Compra.objects.get(pk=self.kwargs['compra_pk'])
        detalle_compra.compra = compra

        # Crea la transacción
        transaccion = Transaccion.objects.create(
            tipo='Entrada',
            producto=detalle_compra.producto,
            cantidad=detalle_compra.cantidad,
            fecha=compra.fecha_compra,
            referencia_compra=str(compra.id) # Referencia a la compra
        )
        detalle_compra.transaccion = transaccion
        
        detalle_compra.save()
        return super().form_valid(form)



class DetalleCompraUpdateView(UpdateView):
    model = DetalleCompra
    fields = ['producto', 'cantidad', 'precio_unitario']
    template_name = 'detallecompra_form.html'

    def get_success_url(self):
         return reverse_lazy('compra_detail', kwargs={'pk': self.object.compra.pk})

    def form_valid(self, form):
        detalle_compra = form.save(commit=False)
        
        # Actualiza la transacción
        transaccion = detalle_compra.transaccion
        transaccion.cantidad = detalle_compra.cantidad # Actualiza the cantidad in Transaccion
        transaccion.save()  # Guarda los cambios de stock del producto

        detalle_compra.save()

        return super().form_valid(form)


class DetalleCompraDeleteView(DeleteView):
    model = DetalleCompra
    template_name = 'detallecompra_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('compra_detail', kwargs={'pk': self.object.compra.pk})


    def delete(self, request, *args, **kwargs):
        detalle_compra = self.get_object()
        
        # Elimina la transacción asociada
        transaccion = detalle_compra.transaccion
        transaccion.delete()
        
        return super().delete(request, *args, **kwargs)


