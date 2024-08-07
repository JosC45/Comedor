"""
URL configuration for Comedor_Untels project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from C1 import views


urlpatterns = [
    path("admin/", admin.site.urls),
    # #path("", views.index, name="indeex"),
    # path("inicio",views.principal,name="inicio"),
    # path("solicitar_cupo",views.solicitarcupo,name="solicitar_cupo"),
    # path("menu",views.vista_menu,name="ver_menu"),
    # path("miscursos",views.my_courses,name="mis_cursos"),
    path("",include('C1.urls')),
    path("accounts/",include("django.contrib.auth.urls")),
]
