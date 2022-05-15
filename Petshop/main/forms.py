from django.forms import ModelForm
from .models import *



class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['nome', 'raca', 'tipo', 'sexo', 'observacoes']

class AtendimentoForm(ModelForm):
    class Meta:
        model = Atendimento
        fields = ['tipo', 'data', 'Descricao', 'animal', 'responsavel']

class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'cpf', 'telefone', 'idade', 'email', 'sexo', 'data_nascimento', 'cargo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})
        self.fields['telefone'].widget.attrs.update({'class': 'mask-telefone'})
        self.fields['data_nascimento'].widget.attrs.update({'class': 'mask-data'})




class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'endereco']