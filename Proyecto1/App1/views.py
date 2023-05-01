from django.shortcuts import render
from App1.models import *
from django.http import HttpResponse
from App1.forms import *

def inicio(request):
    return render(request,'App1/inicio.html')


def tiendas(request):    #Agregar Tiendas
    if request.method =='POST':
        miFormulario=TiendaFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            tienda=Tienda(int(informacion['id']),str(informacion['nombre']),int(informacion['tienda']))
            tienda.save()
            return render(request, 'App1/inicio.html')
    else:
        miFormulario=TiendaFormulario()
    return render(request, 'App1/tiendas.html', {"miFormulario": miFormulario})


def servicios(request): #Agregar Servicios
     if request.method == "POST":
        miFormulario = ServicioFormulario(request.POST) 
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            servicio = Servicio(int(informacion['id']),str(informacion['nombre']),(informacion['fechaentrega']), (informacion['entregado']))
            servicio.save()
            return render(request, "App1/inicio.html")
     else:
        miFormulario = ServicioFormulario()
             
     return render(request, "App1/servicios.html", {"miFormulario": miFormulario})


def empleados(request): #Para agregar empleados a la bd
     if request.method == "POST":
        miFormulario = EmpleadoFormulario(request.POST) 
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            empleado = Empleado(int(informacion['id']),str(informacion['nombre']),str(informacion['apellido']),
                                   informacion['email'], informacion['profesion'])
            empleado.save()
            return render(request, "App1/inicio.html")
     else:
        miFormulario = EmpleadoFormulario()
             
     return render(request, "App1/empleados.html", {"miFormulario": miFormulario})


def clientes(request): #Para agregar clientes a la bd
     if request.method == "POST":
        miFormulario = ClienteFormulario(request.POST) 
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            cliente = Cliente(int(informacion['id']),str(informacion['nombre']),str(informacion['apellido']),informacion['email'])
            cliente.save()
            return render(request, "App1/inicio.html")
     else:
        miFormulario = ClienteFormulario()
             
     return render(request, "App1/clientes.html", {"miFormulario": miFormulario})


#Buscan |

def busquedaTienda(request):   #Para buscar desde la BD
     return render(request,'App1/busquedaTienda.html')

def buscar(request):
     if request.GET['tienda']:
          tienda = request.GET['tienda']
          tiendas= Tienda.objects.filter(tienda__icontains=tienda)

          return render(request,'App1/resultadosBusqueda.html', {"tiendas":tiendas, "Nros": tienda })
     else:
          respuesta= "No enviaste datos"

     return HttpResponse(respuesta)



def busquedaServicio(request):   #Para buscar desde la BD
     return render(request,'App1/busquedaServicio.html')

def buscarServicio(request):
     if request.GET['nombre']:
          id = request.GET['nombre']
          servicios= Servicio.objects.filter(id__icontains=id)
          print(servicios)
          return render(request,'App1/resultadosServicio.html', {"servicios":servicios, "Nros": id })
     else:
          respuesta= "No enviaste datos"

     return HttpResponse(respuesta)