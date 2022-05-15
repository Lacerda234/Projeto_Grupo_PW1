from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import *

from main.models import Cliente, Funcionario, Animal

#nome das views segue o padrao: só o nome = deslogado, cli_nome = cliente, fun_cliente = funcionario
def home(request):
    return render(request, 'home.html')

def desl_atendimentos(request):
    return render(request,'servicos.html') 
# def login(request):
#     return render(request, 'registration/login.html')


class login(TemplateView):
    template_name = 'registration/login.html'

#views referentes aos clientes
class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente
    queryset = Cliente.objects.all()
    context_object_name = 'clientes'
    template_name = 'clientes/homecli.html'


class ClienteCreate(CreateView): 
    model = Cliente
    template_name = 'clientes/forms/form.html'
    fields = '__all__'
    success_url = reverse_lazy('url_home')

class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = '__all__'
    template_name = 'clientes/forms/form.html'
    success_url = reverse_lazy('cli_home')


class ClienteDelete(DeleteView):
    queryset = Cliente.objects.all()
    success_url = reverse_lazy('')

#views referentes aos funcionários
class FunList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Funcionario
    queryset = Funcionario.objects.all()
    template_name = 'funcionario/homefun.html'
    context_object_name = 'funcionarios'

class FunCreate(CreateView):
    model = Funcionario
    fields = '__all__'
    success_url = reverse_lazy('')

class FunUpdate(LoginRequiredMixin, UpdateView):
    model = Funcionario
    fields = '__all__'
    template_name = 'funcionario/formuptFuncionario.html'
    success_url = reverse_lazy('url_homeFun')

class FunDelete(DeleteView):
    queryset = Funcionario.objects.all()
    success_url = reverse_lazy('')


class FunClienteList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Cliente
    queryset = Cliente.objects.all()
    context_object_name = 'clientes' 
    template_name = 'funcionario/clientes.html'


#views referentes aos animais
class AnimalList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Animal
    queryset = Animal.objects.all()
    template_name = 'funcionario/animal.html'
    context_object_name = 'animais'

class AnimalCreate(LoginRequiredMixin, CreateView):
    model = Animal
    fields = '__all__'
    template_name = 'funcionario/formaddAnimal.html'
    success_url = reverse_lazy('url_animais')

class AnimalUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Animal
    fields = '__all__'
    success_url = reverse_lazy('url_animais')
    template_name = 'funcionario/formUptAnimal.html'

class AnimalDetail(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    queryset = Animal.objects.all()

class AnimalDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    template_name = 'funcionario/formUptAnimal.html'
    model = Animal
    success_url = reverse_lazy('url_animalFun')



#views referentes aos Atendimentos
class atendimentoListFun(LoginRequiredMixin, ListView):
    model = Atendimento
    queryset = Atendimento.objects.all()
    template_name = 'funcionario/atendimentos.html'
    context_object_name = 'atendimentos'


class AtendimentoCreateFun(CreateView): 
    model = Atendimento
    template_name = 'funcionario/formAddAtendimento.html'
    fields = '__all__'
    success_url = reverse_lazy('url_atendimentos')

class AtendimentoUpdateFun(LoginRequiredMixin, UpdateView):
    model = Atendimento
    fields = '__all__'
    success_url = reverse_lazy('url_atendimentos')
    template_name = 'funcionario/formUptAtendimento.html'



class AtendimentoDeleteFun(LoginRequiredMixin, DeleteView):
    template_name = 'funcionario/formUptAnimal.html'
    model = Animal
    success_url = reverse_lazy('url_atendimentos')




class atendimentoListCli(LoginRequiredMixin, ListView):
    model = Atendimento
    queryset = Atendimento.objects.all()
    template_name = 'clientes/atendimentos.html'
    context_object_name = 'atendimentos'

class AtendimentoCreateFunCli(CreateView): 
    model = Atendimento
    template_name = 'clientes/formAddAtendimento.html'
    fields = '__all__'
    success_url = reverse_lazy('url_atendimentosCli')

class AtendimentoUpdateCli(LoginRequiredMixin, UpdateView):
    model = Atendimento
    fields = '__all__'
    success_url = reverse_lazy('url_atendimentosCli')
    template_name = 'clientes/formUptAtendimento.html'



class AtendimentoDeleteCli(LoginRequiredMixin, DeleteView):
    template_name = 'clientes/formUptAnimal.html'
    model = Animal
    success_url = reverse_lazy('url_atendimentosCli')




class AnimalCreateCli(LoginRequiredMixin, CreateView):
    model = Animal
    fields = '__all__'
    template_name = 'clientes/formaddAnimal.html'
    success_url = reverse_lazy('url_animaisCli')

class AnimalListCli(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Animal
    queryset = Animal.objects.all()
    template_name = 'clientes/animal.html'
    context_object_name = 'animais'

class AnimalUpdateCli(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Animal
    fields = '__all__'
    success_url = reverse_lazy('url_animaisCli')
    template_name = 'clientes/formUptAnimal.html'

class AnimalDeleteCli(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    template_name = 'clientes/formUptAnimal.html'
    model = Animal
    success_url = reverse_lazy('url_animaisCli')

#View da Tela de contato 
class contato(TemplateView):
    template_name = 'contato.html'
