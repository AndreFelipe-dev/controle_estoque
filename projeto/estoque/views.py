from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return HttpResponse('<h1> Página inicial do projeto</h1>')

pass


def cadastro (request):
    return HttpResponse('<h1> Página de cadastro do projeto</h1>')

pass


def lista (request):
    return HttpResponse('<h1> Página de lista do projeto</h1>')

pass

def busca(request):
    return HttpResponse('<h1> Página de busca do projeto</h1>')

pass