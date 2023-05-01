from django.urls import path 
from App1 import views 

urlpatterns=[

    path('', views.inicio, name="Inicio"), #Inicio

    path('tiendas', views.tiendas, name="Tiendas"),  #Agrega 
    path('empleados', views.empleados, name="Empleados"), #Agrega
    path('clientes', views.clientes, name="Clientes"), #Agrega
    path('servicios', views.servicios, name="Servicios"), #Agrega 


    path('busquedaTienda', views.busquedaTienda, name="BusquedaTienda"), #Busca
    path('busquedaServicio', views.busquedaServicio, name="BusquedaServicio"), #Busca
    path('buscar/',views.buscar), #Busca
    path('buscarServicio/', views.buscarServicio), #Busca

]