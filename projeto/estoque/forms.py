from django import forms

class CadastroForm(forms.Form):

    codigo= forms.IntegerField(required=False,widget=forms.HiddenInput())
    nome= forms.CharField(label='Nome :', max_length=50,
                          widget=forms.TextInput(attrs={'class': 'form-control',  'placeholder':'produto'}))
    preco = forms.FloatField(label='Preço :',
                             widget=forms.TextInput(attrs={'class': 'form-control' ,'type': 'number','placeholder':'R$00,00'}))
    quantidade = forms.IntegerField(label='Quantidade:',
                                    widget=forms.TextInput(attrs={'class': 'form-control' ,
                                                                  'type': 'number','placeholder':'0000'}))


    pass