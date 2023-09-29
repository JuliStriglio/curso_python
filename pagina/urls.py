from django.urls import path 
from pagina.views import inicio, agregar_profesor, buscar_profesor




urlpatterns = [
    
    path('', inicio),
    path('profesor/crear', agregar_profesor , name = 'crear_curso'),
    path('profesor/listado', buscar_profesor, name = 'agregar_profesor'),
]
