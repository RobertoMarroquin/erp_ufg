from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from models import Categoria

class ProductoListView(ListView):
    model = Categoria
    template_name = ''