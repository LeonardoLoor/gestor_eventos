from django.db import models
from eventos.models import Evento
from usuarios.models import Usuario

# Definimos el modelo de Inscripción, que representa la inscripción de un usuario a un evento.
class Inscripcion(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)  # Relación con el modelo Evento
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Relación con el modelo Usuario
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)  # Fecha y hora de la inscripción, se establece automáticamente al crear la inscripción

    def __str__(self):
        return f"{self.usuario.nombre} - {self.evento.nombre}"  # Representación en cadena del objeto Inscripcion
