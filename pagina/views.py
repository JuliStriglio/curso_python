from django.shortcuts import render, redirect
from django.template import Template,Context
from django.http import HttpResponse
from pagina.models import Profesor
from pagina.forms import agregarProfesorForm, busquedaProfesorForm , editarProfesorFormulario
from django.contrib.auth.decorators import login_required, user_passes_test



 
    

def inicio(request) : 
    
    return render(request , r'pagina\inicio.html' )

#AGREGAR PROFESOR#################################################################


def agregar_profesor(request) :
  
    if request.method == 'POST' :
        formulario = agregarProfesorForm(request.POST, request.FILES)
        if formulario.is_valid(): 
            data= formulario.cleaned_data
            profesor = Profesor(nombre=data.get('nombre'), legajo=data.get('legajo'), email=data.get('email'), fecha_nac = data.get('fecha_nac'), avatar = data.get('avatar'), link = data.get('link'))
            profesor.save()
            return redirect("profesores")
        else : 
            return render(request, r'pagina\agregar_profesor.html', {'formulario' : formulario})
            
    formulario = agregarProfesorForm()
    return render(request, r'pagina\agregar_profesor.html', {'formulario' : formulario})


#DETALLAR PROFESOR##########################################################################

def detalle_profesor (request, profe_id) :
    
    profesor=Profesor.objects.get(id=profe_id)
    return render(request, 'pagina/detalle_profesor.html', {'profesor': profesor})

#ELIMINAR PROFESOR##########################################################################

@login_required
def eliminar_profesor(request, profe_id): 
    profe_a_eliminar=Profesor.objects.get(id=profe_id)
    profe_a_eliminar.delete()

    
    return redirect('profesores')

#EDITAR PROFESOR##############################################################################

@login_required
def editar_profesor(request, profe_id):
     profesor_a_editar=Profesor.objects.get(id=profe_id)
    
     if request.method == 'POST':
        formulario = editarProfesorFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            data = formulario.cleaned_data
            profesor_a_editar.nombre = data['nombre'] 
            profesor_a_editar.legajo = data['legajo'] 
            profesor_a_editar.email = data['email']
            profesor_a_editar.fecha_nac = data['fecha_nac']
            profesor_a_editar.avatar = data['avatar']
            profesor_a_editar.link = data['link']
            profesor_a_editar.save()
            return redirect('profesores')
        else:
            return render(request, 'pagina/editar_profesor.html', {'formulario': formulario})
    
     formulario = editarProfesorFormulario(initial={'nombre': profesor_a_editar.nombre, 'legajo' : profesor_a_editar.legajo, 'email' : profesor_a_editar.email, 'fecha_nac' : profesor_a_editar.fecha_nac, 'avatar' : profesor_a_editar.avatar, 'link' : profesor_a_editar.link})
     return render(request, r'pagina\editar_profesor.html', {'formulario': formulario})



#LISTADO PROFESORES##############################################################################

def buscar_profesor(request) :
     formulario = busquedaProfesorForm(request.GET)
     if formulario.is_valid(): 
      nombre_a_buscar= formulario.cleaned_data.get('nombre')
      profe_encontrados = Profesor.objects.filter(nombre__icontains=nombre_a_buscar)

     else : 
         profe_encontrados = Profesor.objects.all()
            
     formulario = busquedaProfesorForm()
     return render(request, r'pagina\listado_profesor.html', { 'formulario' : formulario, 'profe_encontrados' : profe_encontrados})
 
 

def acerca_de_mi(request) : 
     return render(request, 'pagina/about.html')