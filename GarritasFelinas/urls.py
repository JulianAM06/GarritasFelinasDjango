"""
URL configuration for GarritasFelinas project.

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
from django.urls import path, include
from myApp.views import main
from myApp.views import store
from myApp.views import about
from myApp.views import signup
from myApp.views import adopt
from myApp.views import exit
from myApp.views import register
from myApp.views import cart
from myApp.views import agregar_producto, eliminar_producto, restar_producto, limpiar_carrito



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('store/',store),
    path('about/',about),
    path('signup/',signup),
    path('adopt/',adopt),
    path('accounts/', include ('django.contrib.auth.urls')),
    path('logout/', exit, name='exit'),
    path('register/', register),
    path('cart/', cart),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="Cls"),
   
]
