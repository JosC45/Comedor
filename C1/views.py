from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect
#from templates import 

from .models import *
from .forms import *
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    return render(request,'registration/login.html')
# Create your views here.
# def guardar_cupo():
#     if request.method == 'GET':
#         opciones=request.GET['opciones_u']
#         cupos=Cupos(
#             opciones= opciones,
#         )
#         cupos.save()

#         return HttpResponse(f"Cupo guardado con exito")
@login_required
def principal(request):
    return render(request,'inicio.html')
def cupo(request):
    return render(request,'solicitar_cupo.html')

def solicitarcupo(request):
    usuario=request.user.username
    pedidos=detalle_menu.objects.select_related('id_menu__id_dia','id_menu__id_tipo','codigo').filter(codigo=usuario)
    formcupo=selects_cupo
    formdia=selects_dia
    return render(request,'solicitar_cupo.html',{'formcupo':formcupo,'formdia':formdia,'pedidos': pedidos})


def my_courses(request):
    return render(request,'mis_cursos.html')

def buscar(request):
    cantidades=0
    formdia=selects_dia
    if request.method == 'POST':
        formcupo=selects_cupo(request.POST)
        if formcupo.is_valid():
            tipod = formcupo.cleaned_data['type']
            cantidades=Tipo_Menu.objects.filter(tipo=tipod.tipo)     
        else:
            cantidades="No es valido el form"
            print(formcupo.errors)
    else:
        formcupo=selects_cupo()
    return render(request,'solicitar_cupo.html',{'formcupo':formcupo,'formdia':formdia,'cantidadd':cantidades})


# def cupos(request):
#     cupos=Tipo_Menu.objects.all()
#     dias=Dia.objects.values_list('dia',flat="True").distinct
#     return render(request,'solicitar_cupo.html',{'cupos':cupos},{'dias':dias})

# def obtenerdia(request):
#     dias=Dia.objects.values_list('dia',flat="True").distinct
#     return render(request,'solicitar_cupo.html',{'dia':dias})
def cancelarr():
    detalle_menu.cancelar()
    Tipo_Menu.devolver()
    return render(request,'ver_menu.html')

def vista_menu(request):
    Dias_S=Dia.objects.all()
    # Desayuno=Menu.objects.filter(id_semana=1).distinct
    Desayuno=Menu.objects.filter(id_tipo="1").all()
    Almuerzo=Menu.objects.filter(id_tipo='2').all()
    Lonche=Menu.objects.filter(id_tipo="3").all()
    return render(request,'ver_menu.html',{'dia_s':Dias_S,'desayuno':Desayuno,'almuerzo':Almuerzo,'lonche':Lonche})

def save(request):
    form_dia=selects_dia
    form_tipo=selects_cupo
    if request.method=='POST':
        id_d=form_dia.cleaned_data['day']
        id_t=form_tipo.cleaned_data['type']
        id_di=id_d.id
        id_tip=id_t.id
    if id_di and id_tip:
        try:
            menu=Menu.objects.get(id_semana=1,id_dia=id_di,id_tipo=id_tip)
        except ObjectDoesNotExist:
            error = "No se encontró ninguna reserva con ese nombre y fecha."
        except Tipo_Menu.MultipleObjectsReturned:
            error = "Se encontraron múltiples reservas con ese nombre y fecha."
            if menu:
                menu_id=menu.id
                codigo=request.user.username
                detalle=detalle_menu(
                    codigo_id=codigo,
                    id_menu_id=menu_id,
                )
                detalle.save()
            else:
                print("No se pudo agregar el detalle")
    return HttpResponse(f"Detalle Menu agregado: {detalle.codigo} - {detalle.id_menu}")
def exit(request):
    logout(request)
    return redirect('inicio')
