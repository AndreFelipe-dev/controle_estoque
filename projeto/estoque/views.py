import json

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
    #SELECT * FROM
    produtos = Produto.objects.all()
    return render(request, 'estoque/lista.html', { 'produtos' : produtos})

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

                if form.cleaned_data['codigo'] is not None:
                    produto.codigo = form.cleaned_data['codigo']
                    print(produto.codigo)

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


def excluir(request,codigo):

    try:
        produto = Produto.objects.get(pk=codigo)
        result = produto.delete()
        if result[0] > 0:
            msg = 'Produto deletado com sucesso '

        else:
            msg = 'Produto não encontrado'

        produtos = Produto.objects.all()
        return render(request, 'estoque/lista.html', {'produtos': produtos, 'msg': msg })


    except Exception as ex:
        produtos = Produto.objetcs.all()
        msg= ex.args
        return render(request, 'estoque/lista.html', { 'produtos': produtos, 'msg': msg})
    pass

def alterar(request,codigo):
    try:
        produto = Produto.objects.get(pk=codigo)
        form = CadastroForm(initial={
            'codigo': produto.codigo,
            'nome' : produto.nome,
            'preco': produto.preco,
            'quantidade': produto.quantidade,
        })



        return render(request, 'estoque/cadastro.html', {'form': form})


    except Exception as ex:
        produtos = Produto.objetcs.all()
        msg = ex.args
        return render(request, 'estoque/lista.html', {'produtos': produtos, 'msg': msg})
    pass


def pesquisar(request):

    try:
        if request.method== 'POST':
            nome = request.POST['nome']
            produtos = Produto.objects.filter(nome__icontains= nome)

            response = {}

            for indice, produto in enumerate(produtos):

                p= {}

                p ['codigo'] = produto.codigo
                p ['nome'] = produto.nome
                p ['preco'] = produto.preco
                p ['quantidade'] = produto.quantidade

                response[indice]= p

            response['t'] = len(produtos)

            return HttpResponse(json.dumps(response), content_type='application/json')




    except Exception as ex:
        msg = ex.args
        return HttpResponse(json.dumps({"msg": msg}), content_type = 'application/json')

    pass