from django.urls import path
from .import views

app_name = 'estoque'

urlpatterns =[

    path('' ,views.home, name ='home'),
    path('Cadastro/' , views.cadastro, name ='cadastro'),
    path('Lista/' , views.lista, name ='busca'),
    path('Busca/' , views.busca, name ='busca')

    ]

