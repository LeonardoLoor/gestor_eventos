from django.urls import path
from . import views

urlpatterns = [
    path('inscribir/<int:evento_id>/', views.inscribir, name='inscribir'),
    path('mis_eventos/', views.mis_eventos, name='mis_eventos'),
]
