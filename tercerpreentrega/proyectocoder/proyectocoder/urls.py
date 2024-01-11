"""
URL configuration for proyectocoder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from apptiendafutbol.views import *
urlpatterns = [
    
    path('admin/', admin.site.urls),

    path("",inicio, name = "inicio"),
    path('nueva_camisetas', pedir_camiseta, name = "camiseta"),
    path('nuevo_shorts', pedir_shorts, name = "shorts"), 
    path('nuevo_botines', pedir_botines, name = "botines"),

    
    #path('nueva_camisetas', pedir_camiseta), 
    #path('nuevo_shorts', pedir_shorts),
    #path('nuevo_botines', pedir_botines),
]
