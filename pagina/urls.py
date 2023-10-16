from django.urls import path 
from pagina.views import inicio, agregar_profesor, buscar_profesor, detalle_profesor, editar_profesor, eliminar_profesor




urlpatterns = [
    
    path('', inicio, name = 'inicio'),
    path('profesor/crear', agregar_profesor , name = 'agregar_profesor'),
    path('profesor/<int:profe_id>/detalle', detalle_profesor , name = 'detalle_profesor'),
    path('profesor/<int:profe_id>/editar', editar_profesor , name = 'editar_profesor'),
    path('profesor/listado', buscar_profesor, name = 'profesores'),
    path('profesor/<int:profe_id>/eliminar', eliminar_profesor , name = 'eliminar_profesor'),
]
