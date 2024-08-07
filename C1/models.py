from datetime import timezone
from django.db import models

class Alumno(models.Model):
    codigo=models.CharField(max_length=8, primary_key=True)
    password=models.IntegerField(null=True)
    nombres=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    Carrera=models.CharField(max_length=30)
    Estado=models.BooleanField(default=True)

    def __str__(self):
        return self.codigo

class Dia(models.Model):
    dia=models.CharField(max_length=20)
    def __str__(self):
        return self.dia

class Semana(models.Model):
    semana=models.IntegerField(db_index=True)
    def __str__(self):
        semana1=str(self.semana)
        return semana1
class Tipo_Menu(models.Model):
    tipo=models.CharField(max_length=20)
    cantidad=models.IntegerField(null=True)
    def __str__(self):
        return self.tipo
    def devolver(self):
        if self.cantidad<=150:
            self.cantidad+=1
            self.save()
        else:
            return "No se puede cancelar cupo"
        
class Menu(models.Model):
    id_semana=models.ForeignKey(Semana,on_delete=models.CASCADE)
    id_dia=models.ForeignKey(Dia,on_delete=models.CASCADE)
    id_tipo=models.ForeignKey(Tipo_Menu,on_delete=models.CASCADE)
    bebida=models.CharField(max_length=30)
    comida=models.CharField(max_length=30)
    def __str__(self):
        return self.comida

class detalle_menu(models.Model):
    id_detalle_menu=models.AutoField(primary_key=True)
    codigo=models.ForeignKey(Alumno,on_delete=models.CASCADE,to_field='codigo')
    id_menu=models.ForeignKey(Menu,on_delete=models.CASCADE)
    value=models.BooleanField(default=True)
    def __str__(self):
        return self.id_detalle_menu
    def cancelar(self):
        self.value=False
        self.save()
        return self.value
 

