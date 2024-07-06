from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Manager personalizado para el modelo de usuario
class UsuarioManager(BaseUserManager):
    def create_user(self, email, nombre, password=None):
        if not email:
            raise ValueError("El usuario debe tener un correo electrónico")
        usuario = self.model(email=self.normalize_email(email), nombre=nombre)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, nombre, password):
        usuario = self.create_user(email, nombre, password)
        usuario.is_admin = True
        usuario.save(using=self._db)
        return usuario

# Modelo personalizado de usuario
class Usuario(AbstractBaseUser):
    email = models.EmailField(verbose_name="Correo Electrónico", max_length=255, unique=True)
    nombre = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
