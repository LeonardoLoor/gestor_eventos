from django.db import models
from usuarios.models import Usuario

class Evento(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=255)
    fecha_hora = models.DateTimeField()
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
