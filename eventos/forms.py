from django import forms
from .models import Evento

# Defino el formulario para el modelo Evento
class EventoForm(forms.ModelForm):
    # Campo personalizado para fecha y hora con tipo de input datetime-local
    fecha_hora = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )
    # Campo personalizado para la ubicación con un placeholder específico
    ubicacion = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Selecciona la Ubicación'})
    )

    class Meta:
        model = Evento
        fields = ['nombre', 'descripcion', 'ubicacion', 'fecha_hora']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Evento'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del Evento'}),
        }
