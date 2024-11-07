from .models import Usuario
from rest_framework import generics
from .serializers import UsuarioSerializer, UsuarioUpdateSerializer

# Create your views here.

# Para Listar Y Crear Nuevos Usuarios maneja get y post
class UsuariosList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Para consultar y actualizar un solo Usuario maneja get, put delete
class UserList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioUpdateSerializer
    lookup_field = 'email'


