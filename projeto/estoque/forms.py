from django import forms

class CadastroForm(forms.Form):

    nome= forms.CharField(label='Digite seu nome ', max_length=50)
    preco = forms.FloatField(label='Digite o preço',)
    quantidade = forms.IntegerField(label='Digite a quantidade ')


    pass