from django.db import models

class Produto(models.Model): #Mapeamento da classe como tabela


    codigo= models.AutoField (primary_key=True) #chave primária
    nome= models.CharField(max_length=(100 ),null=False)  #null false == Não pode ser nulo
    preco =models.FloatField(null=False)
    quantidade = models.IntegerField(null=False)

    def __int__(self, codigo = None,nome = None, preco= None, quantidade = None ):
        models.Model.__init__(self)

        self.codigo = codigo
        self.nome = nome
        self.preco= preco
        self.quantidade = quantidade

    def __str__(self):
        return '{},{},{},{}'.format(self.codigo,self.nome,self.preco,self.quantidade)

    def __repr__(self):
        return '{},{},{},{}'.format(self.codigo,self.nome,self.preco,self.quantidade)

