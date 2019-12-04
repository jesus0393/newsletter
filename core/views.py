from django.contrib.auth.models import User
from rest_framework import viewsets
from core.serializers import UserSerializer, CreateUserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    retive: 
        Regresa la instancia de un usuario
    list:
        Regresa la lista de usuarios
    update:
        actualiza un usuario
    partial_update:
        actualiza un campo en particular de un usuario
    delete:
        Elimina un usuario
    """
    
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateUserSerializer
        return UserSerializer