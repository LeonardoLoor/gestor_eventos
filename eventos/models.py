from django.db import models
from django.conf import settings

class Evento(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=255)
    fecha_hora = models.DateTimeField()
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    inscritos = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='eventos_inscritos', blank=True)

    def __str__(self):
        return self.nombre
