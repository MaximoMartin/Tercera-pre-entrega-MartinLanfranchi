from django import forms
 
class TiendaFormulario(forms.Form):
    id= forms.IntegerField()
    nombre = forms.CharField()
    tienda = forms.IntegerField()

class ClienteFormulario(forms.Form):
    id = forms.IntegerField()
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()


class EmpleadoFormulario(forms.Form):
    id = forms.IntegerField()
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)


class ServicioFormulario(forms.Form):
    id = forms.IntegerField()
    nombre = forms.CharField(max_length=30)
    fechaentrega = forms.DateField()    # fecha es 2023-12-31
    entregado = forms.BooleanField()