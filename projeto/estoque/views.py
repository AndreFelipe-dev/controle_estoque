from django.shortcuts import render, HttpResponse,loader

from .forms import CadastroForm
from .models import Produto
#Dentro da views é onde declaramos todas as regras de negócio do sistema

def home(request):

    templates = loader.get_template('estoque/home.html')
    return HttpResponse(templates.render())


def cadastro(request):
    form = CadastroForm()

    return render(request, 'estoque/cadastro.html', {'form': form})



def lista (request):
    return render(request, 'estoque/lista.html')

    pass

def busca(request):
    return render(request, 'estoque/busca.html')

    pass

def cadastrar(request):

    try:
        if request.method == 'POST':
            form = CadastroForm(request.POST)
            if form.is_valid():
                #CADASTRAR O PRODUTO
                produto = Produto()
                produto.nome = form.cleaned_data['nome']
                produto.preco = form.cleaned_data['preco']
                produto.quantidade = form.cleaned_data['quantidade']

                produto.save()

                msg = 'Produto cadastradado com sucesso '
                return render(request, 'estoque/cadastro.html', {'form': CadastroForm(), 'msg': msg})

            else:msg= form.errors
            return render(request,' estoque/cadastro.html', {'form': form, 'msg': msg})

        else:
            raise Exception('MethodEnvioError,Use POST para formulário')

    except Exception as ex:
        msg = ex.args
        return render(request, 'estoque/cadastro.html', {'form': CadastroForm(), 'msg': msg})


    pass

