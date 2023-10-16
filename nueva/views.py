from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from nueva.models import Materia
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class MateriaCreateView(CreateView):
    model = Materia
    template_name = "nueva/agregar_materia.html"
    fields = ['nombre', 'dia_cursado', 'descripcion', 'fecha_parcial']
    success_url = reverse_lazy('materias') 
    
    
class MateriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Materia
    template_name = "nueva/eliminar_materia.html"
    success_url = reverse_lazy('materias') 
    
class MateriaDetailView(DetailView):
    model = Materia
    template_name = "nueva/detalle_materia.html"


class MateriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Materia
    template_name = "nueva/editar_materia.html"
    fields = ['nombre', 'dia_cursado', 'descripcion', 'fecha_parcial']
    success_url = reverse_lazy('materias') 
    

class MateriaListView(ListView):
    model = Materia
    template_name = "nueva/listado_materias.html"
    context_object_name = 'listar_materias'
    
    def get_queryset(self):
       nombre = self.request.GET.get('nombre', '')
       if nombre:
           materias = self.model.objects.filter(nombre__icontains=nombre)
       else:
        materias = self.model.objects.all()
        return materias