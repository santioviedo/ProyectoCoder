from django import forms

class camisetaformulario (forms.Form):
    equipo = forms.CharField(max_length=30)
    talle = forms.CharField(max_length=30)
    año = forms.IntegerField()
    tipo = forms.CharField(max_length=30)

class shortformulario (forms.Form):
    equipo = forms.CharField(max_length=30)
    talle = forms.CharField(max_length=30)
    año = forms.IntegerField()
    tipo = forms.CharField(max_length=30)

class botinesformulario (forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    talle = forms.CharField(max_length=30)