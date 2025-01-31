from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario

# Formulario de registro de usuario, basado en UserCreationForm
class RegistroForm(UserCreationForm):
    # Campo de email
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@domain.com'}),
        error_messages={
            'required': 'Este campo es obligatorio.',
            'invalid': 'Ingrese un correo electrónico válido.'
        }
    )
    # Campo de nombre
    nombre = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu Nombre'}),
        error_messages={
            'required': 'Este campo es obligatorio.'
        }
    )
    # Campo de contraseña
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
        error_messages={
            'required': 'Este campo es obligatorio.',
        }
    )
    # Campo de confirmación de contraseña
    password2 = forms.CharField(
        label="Confirmar Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar Contraseña'}),
        error_messages={
            'required': 'Este campo es obligatorio.',
            'password_mismatch': 'Las contraseñas no coinciden.'
        }
    )

    class Meta:
        model = Usuario
        fields = ['email', 'nombre', 'password1', 'password2']

    # Validación personalizada para el campo email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado.')
        return email
    
    # Sobrescribir el método save para guardar el usuario correctamente
    def save(self, commit=True):
        user = super(RegistroForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.nombre = self.cleaned_data["nombre"]
        if commit:
            user.save()
        return user

# Formulario de inicio de sesión de usuario, basado en AuthenticationForm
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu Usuario'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
    )
