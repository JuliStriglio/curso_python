from django.urls import path
from nueva import views

urlpatterns = [
    
    path('materias/', views.MateriaListView.as_view() , name= 'materias'),
    path('materias/crear', views.MateriaCreateView.as_view(), name = 'agregar_materia'),
    path('materias/<int:pk>/', views.MateriaDetailView.as_view() , name = 'detalle_materia'),
    path('materias/<int:pk>/editar',views.MateriaUpdateView.as_view(), name = 'editar_materia'),
    path('materias/<int:pk>/eliminar', views.MateriaDeleteView.as_view(), name = 'eliminar_materia'),
    
]
