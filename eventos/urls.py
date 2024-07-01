from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),
    path('crear/', views.crear_evento, name='crear_evento'),
    path('<int:evento_id>/', views.detalle_evento, name='detalle_evento'),
    path('<int:evento_id>/editar/', views.editar_evento, name='editar_evento'),
    path('<int:evento_id>/eliminar/', views.eliminar_evento, name='eliminar_evento'),
    path('<int:evento_id>/inscribirse/', views.inscribirse_evento, name='inscribirse_evento'),  # Añadir esta línea
]
