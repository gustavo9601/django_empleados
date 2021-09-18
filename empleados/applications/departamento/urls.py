from django.urls import path
from .views import DepartamentoView

def desdeApps(self):
    print("ss")

url_departameto = [
    path('departamento/', desdeApps),
    path('new-departamento/', DepartamentoView.as_view(), name='new_department'),
]
