from django.shortcuts import render
from django.template import Template,Context
from django.http import HttpResponse
from pagina.models import Profesor
from pagina.forms import agregarProfesorForm, busquedaProfesorForm



# Create your views here.

def inicio(request) : 
    
    #return render(request , r'pagina\templates\pagina\inicio.html' , {})
    return render(request , r'pagina\inicio.html' )

def agregar_profesor(request) :
  
    if request.method == 'POST' :
        formulario = agregarProfesorForm(request.POST)
        if formulario.is_valid(): 
            data= formulario.cleaned_data
            curso = Profesor(nombre=data.get('nombre'), legajo=data.get('legajo'))
            curso.save()
        else : 
            return render(request, r'pagina\agregar_profesor.html', {'formulario' : formulario})
            
    formulario = agregarProfesorForm()
    return render(request, r'pagina\agregar_profesor.html', {'formulario' : formulario})


def buscar_profesor(request) :
     formulario = busquedaProfesorForm(request.GET)
     if formulario.is_valid(): 
      nombre_a_buscar= formulario.cleaned_data.get('nombre')
      profe_encontrados = Profesor.objects.filter(nombre__icontains=nombre_a_buscar)

     else : 
         profe_encontrados = Profesor.objects.all()
            
     formulario = busquedaProfesorForm()
     return render(request, r'pagina\listado_profesor.html', { 'formulario' : formulario, 'profe_encontrados' : profe_encontrados})