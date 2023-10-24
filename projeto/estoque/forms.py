from django import forms

class CadastroForm(forms.Form):

    codigo= forms.IntegerField(required=False,widget=forms.HiddenInput())
    nome= forms.CharField(label='Nome :', max_length=50,
                          widget=forms.TextInput(attrs={'class': 'form-control', }))
    preco = forms.FloatField(label='Preço :',
                             widget=forms.TextInput(attrs={'class': 'form-control' ,'type': 'number'}))
    quantidade = forms.IntegerField(label='Quantidade:',
                                    widget=forms.TextInput(attrs={'class': 'form-control' ,'type': 'number'}))


    pass