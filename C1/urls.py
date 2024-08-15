from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
from .api import AlumnoViewSet,MenuViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'alumno',AlumnoViewSet)
router.register(r'menu',MenuViewSet)

# router=routers.DefaultRouter()
# router.register('api/alumno',AlumnoViewSet,'alumno')

urlpatterns = [
    #path("", views.index, name="indeex"),
    path('',views.principal,name="inicio"),
    path("solicitar_cupo/",views.solicitarcupo,name="solicitar_cupo"),
    path('solicitar_cupo/search/',views.buscar,name="buscar"),
    path("menu/",views.vista_menu,name="ver_menu"),
    path("miscursos/",views.my_courses,name="mis_cursos"),
    path("exit/",views.exit,name="exit"),
    path("vista_menu/",views.vista_menu,name="vista_menu"),
    path("guardar_detalle/",views.save,name="save_detalle"),
    #path("cancelar_pedido/",views.cancelarr,name="cancelar")
    path("api/",include(router.urls))
]