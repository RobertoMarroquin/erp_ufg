from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from inventario.models import Transaccion, Producto

class TransaccionListView(ListView):
    model = Transaccion
    template_name = 'transaccion_list.html'
    context_object_name = 'transacciones'
    ordering = ['-fecha']  # Ordenar por fecha descendente (más recientes primero)


class TransaccionDetailView(DetailView):
    model = Transaccion
    template_name = 'transaccion_detail.html'
    context_object_name = 'transaccion'



class TransaccionCreateView(CreateView):  #Para crear manualmente una transaccion
    model = Transaccion
    template_name = 'transaccion_form.html'
    fields = ['tipo', 'producto', 'cantidad', 'fecha', 'referencia_compra', 'referencia_venta']
    success_url = reverse_lazy('transaccion_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.actualizar_stock_producto()  # Actualizar stock después de guardar
        return response



class TransaccionUpdateView(UpdateView):  #Para editar manualmente una transaccion
    model = Transaccion
    template_name = 'transaccion_form.html'
    fields = ['tipo', 'producto', 'cantidad', 'fecha', 'referencia_compra', 'referencia_venta']
    success_url = reverse_lazy('transaccion_list')

    def form_valid(self, form):

        # Obtener la transacción original antes de guardar los cambios
        old_transaction = Transaccion.objects.get(pk=self.object.pk)

        # Calcular la diferencia en la cantidad
        cantidad_difference = self.object.cantidad - old_transaction.cantidad


        # Revertir la actualización del stock de la transacción antigua
        old_transaction.producto.stock -= old_transaction.cantidad
        if old_transaction.tipo == 'Entrada':
            old_transaction.producto.stock -= cantidad_difference
        else:
            old_transaction.producto.stock += cantidad_difference

        
        old_transaction.producto.save()

        #Aplicar cambios
        response = super().form_valid(form)

        # Actualizar el stock con los nuevos valores
        self.object.actualizar_stock_producto()
        return response

class TransaccionDeleteView(DeleteView):
    model = Transaccion
    template_name = 'transaccion_confirm_delete.html'
    success_url = reverse_lazy('transaccion_list')


    def delete(self, request, *args, **kwargs):
        transaccion = self.get_object()

        #Revertir la transaccion
        producto = transaccion.producto
        if transaccion.tipo == 'Entrada':
            producto.stock -= transaccion.cantidad
        else:
            producto.stock += transaccion.cantidad
        producto.save()
        return super().delete(request, *args, **kwargs)




