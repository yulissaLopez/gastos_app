from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UsuarioManager

# Create your models here.
class Usuario(AbstractUser):
    "Quito el campo username del modelo"
    username = None
    email = models.EmailField("Correo Electronico", unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UsuarioManager()

    def __str__(self):
        return self.email



