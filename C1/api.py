from .models import *
from rest_framework import viewsets,permissions
from .serializers import AlumnoSerializer,MenuSerializer

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset=Alumno.objects.all()
    permissions_classes=[permissions.IsAuthenticated]
    serializer_class=AlumnoSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset=Menu.objects.all()
    permissions_classes=[permissions.AllowAny]
    serializer_class=MenuSerializer