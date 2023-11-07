from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate,login as django_login
from cuentas.forms import formularioDeRegistro, formularioDeEditarPerfil, formularioCambiarPass, formularioLogin
from django.contrib.auth.views import PasswordChangeView 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from cuentas.models import InfoExtra



#LOGIN#################################################################################

def login(request) : 
    
    
    if request.method == 'POST' : 
        formulario = formularioLogin(request, data=request.POST)
        if formulario.is_valid(): 
            username = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password')
            
            usuario = authenticate(username = username, password = password)
            
            django_login(request, usuario)
            
            InfoExtra.objects.get_or_create(user = usuario)
            
            return redirect('inicio')
    else : 
        formulario = formularioLogin()
    
    return render(request, 'cuentas/login.html', {'formulario' : formulario})


#REGISTRO#########################################################################

def registro (request) :
    
    if request.method == 'POST' :
        formulario = formularioDeRegistro(request.POST)
        if formulario.is_valid() :
            formulario.save()
            return redirect('login')
    else :
        formulario = formularioDeRegistro()
        
    return render(request, 'cuentas/registro.html' , {'formulario' : formulario} )

#EDITAR##############################################################################

@login_required
def editar_perfil (request) : 
        
        info_extra = request.user.infoextra
    
        if request.method == 'POST' :
         formulario = formularioDeEditarPerfil( request.POST,request.FILES, instance=request.user)
         if formulario.is_valid() : 
            
            info_extra.link= formulario.cleaned_data.get('link')
            info_extra.descripcion = formulario.cleaned_data.get('descripcion')
            if formulario.cleaned_data.get('avatar'):
               info_extra.avatar = formulario.cleaned_data.get('avatar')
               
            info_extra.save()
             
            formulario.save()
            return redirect('inicio')
        else : 
          formulario = formularioDeEditarPerfil(initial = {'link' : info_extra.link , 'avatar' : info_extra.avatar, 'descripcion' : info_extra.descripcion} , instance=request.user)
        return render(request, 'cuentas/editar_perfil.html', {'formulario': formulario})
    
#EDITAR_PASS###########################################################################

class CambiarContrasenia (LoginRequiredMixin, PasswordChangeView):
    
    form_class = formularioCambiarPass
    template_name = 'cuentas/editar_pass.html'
    success_url = reverse_lazy('editar_perfil')


#MOSTRAR_DATOS#########################################################################
@login_required
def mostrar_datos (request) : 
    
    if request.user.is_authenticated : 
        
        usuario = request.user
        
        nombre = usuario.first_name
        apellido = usuario.last_name
        email = usuario.email
        
        perfil = InfoExtra.objects.get(user=usuario)
        link = perfil.link
        avatar = perfil.avatar
        descripcion = perfil.descripcion
        
    return render(request, 'cuentas/mostrar_datos.html', {'nombre' : nombre, 'apellido' : apellido, 'email' : email, 'link' : link, 'avatar' : avatar, 'descripcion' : descripcion})

