from django import forms
from .models import Compra, DetalleCompra, Producto


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['fecha_compra', 'proveedor']  # Campos a incluir en el formulario
        widgets = {
            'fecha_compra': forms.DateInput(attrs={'type': 'date'}),  # Widget para la fecha
        }


class DetalleCompraForm(forms.ModelForm):
    class Meta:
        model = DetalleCompra
        fields = ['producto', 'cantidad', 'precio_unitario']
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-control'}),  # Un ejemplo de widget
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),  # Otro ejemplo
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Lógica para modificar el queryset de productos (opcional)
        # self.fields['producto'].queryset = Producto.objects.filter(  # ... alguna condición ...)


#Si prefieres usar forms.Form para el DetalleCompra podrías hacer algo como esto:
class DetalleCompraFormsetHelper(forms.Form):
    producto = forms.ModelChoiceField(queryset=Producto.objects.all())
    cantidad = forms.IntegerField(min_value=1) #Asegurar un valor mínimo de 1
    precio_unitario = forms.DecimalField(decimal_places=2)

# Formset para DetalleCompra (se usa en las vistas)
DetalleCompraFormSet = forms.inlineformset_factory(
    Compra,
    DetalleCompra,
    form=DetalleCompraFormsetHelper,  # Usa el formulario que creamos o ModelForm
    extra=1, # Número de formularios vacíos adicionales para agregar nuevos detalles
    can_delete=True, # Habilitar la eliminación de detalles
)


