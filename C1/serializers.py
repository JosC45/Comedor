from rest_framework import serializers
from .models import *

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ['codigo','password','nombres','apellidos','Carrera']
        read_only_fields=('created_at',)

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu 
        fields = ['id_semana','id_dia','id_tipo','bebida','comida']
        read_only_fields=('created_at',)