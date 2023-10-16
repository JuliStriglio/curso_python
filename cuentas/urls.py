from django.urls import path
from cuentas.views import login, registro, editar_perfil
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('login/', login, name='login' ),
    path('registrarse/', registro , name='registro' ),
    path('perfil/editar/', editar_perfil , name='editar_perfil' ),
    path('logout/', LogoutView.as_view(template_name='cuentas/logout.html'), name='logout' ),
    
]
