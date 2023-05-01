from django.db import models

class Tienda(models.Model):
    nombre= models.CharField(max_length=40)
    tienda= models.IntegerField()

class Cliente(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)
    
class Servicio(models.Model):
    nombre= models.CharField(max_length=30)
    fechaentrega= models.DateField()
    entregado= models.BooleanField()