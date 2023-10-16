from django.urls import path
from .import views
#Rotas das urls

app_name = 'estoque'

urlpatterns =[
    #http://127.0.0.1:8000/ControleEstoque/
    path('',views.home, name='home'),

    # http://127.0.0.1:8000/ControleEstoque/Cadastro
    path('Cadastro/', views.cadastro, name='cadastro'),

    #http://127.0.0.1:8000/ControleEstoque/Lista/
    path('Lista/', views.lista, name='lista'),

    # http://127.0.0.1:8000/ControleEstoque/Busca
    path('Busca/', views.busca, name='busca'),

    #     URL(HTML)    (função do views)     (referência :name)
    path('Cadastrar/', views.cadastrar, name='cadastrar'),

]

