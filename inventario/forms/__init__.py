from django import forms
from django.forms.models import inlineformset_factory
from inventario.models import Compra, DetalleCompra, Producto


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
        fields = ['producto', 'cantidad', 'precio_unitario']  # Define explícitamente los campos
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Lógica opcional para el queryset de producto
        self.fields['producto'].queryset = Producto.objects.all()


# Creación del formset
DetalleCompraFormSet = inlineformset_factory(
    parent_model=Compra,
    model=DetalleCompra,
    form=DetalleCompraForm,  # Usa el ModelForm correcto
    extra=1,  # Formularios adicionales vacíos para agregar detalles
    can_delete=True  # Habilitar eliminación de formularios
)
