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
    return render(request,'solicitar_cupo.html',{'formcupo':formcupo,'pedidos': pedidos})


def my_courses(request):
    return render(request,'mis_cursos.html')

def buscar(request):
    cantidades=0
    if request.method == 'POST':
        formcupo=selects_cupo(request.POST)
        if formcupo.is_valid():
            diad=formcupo.cleaned_data['day']
            tipod = formcupo.cleaned_data['type']
            cantidades=Tipo_Menu.objects.filter(tipo=tipod.tipo)
            diaa=Dia.objects.filter(dia=diad.dia)     
        else:
            cantidades="No es valido el form"
            print(formcupo.errors)
    else:
        formcupo=selects_cupo()
    return render(request,'solicitar_cupo.html',{'formcupo':formcupo,'diaa':diaa,'cantidadd':cantidades})


# def cupos(request):
#     cupos=Tipo_Menu.objects.all()
#     dias=Dia.objects.values_list('dia',flat="True").distinct
#     return render(request,'solicitar_cupo.html',{'cupos':cupos},{'dias':dias})

# def obtenerdia(request):
#     dias=Dia.objects.values_list('dia',flat="True").distinct
#     return render(request,'solicitar_cupo.html',{'dia':dias})

# def cancelarr(request):
#     if request.method=='POST':
#         for_delete=request.menu
#         for_delete.delete()
#         Tipo_Menu.devolver()
#     return HttpResponse("Cupo cancelado")

def vista_menu(request):
    Dias_S=Dia.objects.all()
    # Desayuno=Menu.objects.filter(id_semana=1).distinct
    Desayuno=Menu.objects.filter(id_tipo="1").all()
    Almuerzo=Menu.objects.filter(id_tipo='2').all()
    Lonche=Menu.objects.filter(id_tipo="3").all()
    return render(request,'ver_menu.html',{'dia_s':Dias_S,'desayuno':Desayuno,'almuerzo':Almuerzo,'lonche':Lonche})

def save(request):
    usuario=request.user.username
    pedidos=detalle_menu.objects.select_related('id_menu__id_dia','id_menu__id_tipo','codigo').filter(codigo=usuario)
    form_tipo=selects_cupo
    if request.method=='POST':
        id_d=request.POST.get('day')
        id_t=request.POST.get('hour')
        id_di=Dia.objects.get(dia=id_d)
        id_tip=Tipo_Menu.objects.get(tipo=id_t)
    if id_di and id_tip:
        try:
            menu=Menu.objects.get(id_semana=1,id_dia=id_di.id,id_tipo=id_tip.id)
            print(menu)
        except ObjectDoesNotExist:
            error = "No se encontró ninguna reserva con ese nombre y fecha."
        except Tipo_Menu.MultipleObjectsReturned:
            error = "Se encontraron múltiples reservas con ese nombre y fecha."
            if menu:
                menu_id=menu.id
                print(menu_id)
                codigo=request.user.username
                detalle=detalle_menu(
                    codigo_id=codigo,
                    id_menu_id=menu_id,
                )
                detalle.save()
                context={'detalle':detalle,'pedidos':pedidos}
            else:
                print("No se pudo agregar el detalle")
        #     elif detalle:
        #         if request.method=='POST':
        #             detalle.delete()
        #             Tipo_Menu.devolver()
        #             mensaje="Se elimino el menu seleccionado"
        #             context={'detalle':detalle,'pedidos':pedidos,'mensaje':mensaje}
        # return render(request,'solicitar_cupo.html',context)
def exit(request):
    logout(request)
    return redirect('inicio')
