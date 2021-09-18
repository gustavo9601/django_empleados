from django import forms

from .models import Departamento

class DepartamentoForm(forms.Form):

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    name = forms.CharField(max_length=50)
    short_name = forms.CharField(max_length=20)


