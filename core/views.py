from django.shortcuts import render, redirect
from core.models import Cliente
from core.form import FormCliente
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from django.shortcuts import render

def home(request):
    return render(request, 'core/index.html' )


def cadastrarCliente(request):
    form = FormCliente(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return  redirect('url_listagem')
    else:
        return render(request, 'core/cadastro.html', {'form':form , 'acao': 'Cadastra'})


def listarCliente(request):
    dados = Cliente.objects.all()
    return render(request, 'core/listagem.html' , {'dados': dados})


