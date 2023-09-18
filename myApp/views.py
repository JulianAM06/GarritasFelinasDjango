from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from .forms import CustomUserForm
from myApp.models import Producto
from myApp.carrito import Carrito



def main (request):
    return render (request,'main.html')

def store (request):
    productos = Producto.objects.all()
    return render (request,'store.html', {'productos': productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect ('/store')

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect ('/store')
    
def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect ('/store')

def limpiar_carrito(request):
    carrito = Carrito(request) 
    carrito.limpiar()  
    return redirect ('/store') 
    
def about (request):
    return render (request,'about.html')


@login_required
def adopt (request):
    return render (request,'adopt.html')

def signup (request):
    return render (request, 'signup.html')

def exit (request):
    logout (request)
    return redirect('/')


def register (request): 
    data = {
        'form': CustomUserForm
        
    }
    
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='/')
    
    return render (request, 'registration/register.html', data)

def cart (request):
    return render (request,'cart.html')


    
        
    

