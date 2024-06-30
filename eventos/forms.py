from django import forms
from .models import Evento
from django.utils import timezone

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'descripcion', 'ubicacion', 'fecha_hora']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise forms.ValidationError('Este campo es obligatorio.')
        return nombre

    def clean_fecha_hora(self):
        fecha_hora = self.cleaned_data.get('fecha_hora')
        if fecha_hora < timezone.now():
            raise forms.ValidationError('La fecha y hora del evento no pueden ser en el pasado.')
        return fecha_hora
