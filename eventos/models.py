from django.db import models
from django.conf import settings

# Defino el modelo para los eventos
class Evento(models.Model):
    nombre = models.CharField(max_length=255)  # Nombre del evento
    descripcion = models.TextField()  # Descripción del evento
    ubicacion = models.CharField(max_length=255)  # Ubicación del evento
    fecha_hora = models.DateTimeField()  # Fecha y hora del evento
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Usuario que crea el evento
    inscritos = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='eventos_inscritos', blank=True)  # Usuarios inscritos al evento

    def __str__(self):
        return self.nombre  # Representación en cadena del modelo
