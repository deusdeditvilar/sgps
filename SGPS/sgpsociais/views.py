from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm
from .models import *



def logoff(request):
    logout(request)
    return redirect(settings.LOGIN_URL)

@login_required(login_url='/')
def home(request):
    return render(request, 'inicio.html')

'''
def logon(request, template_name="login.html"):
    next = request.GET.get('next', 'home/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(next)

        else:
            messages.error(request, 'Usuário ou senha incorretos.')
            return HttpResponseRedirect(settings.LOGIN_URL)
    elif
    return render(request, template_name, {'redirect_to': next})
'''

#Assim fica melhor pra autenticar o usuário
def logon(request, template_name="login.html"):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #loga o usuario
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('sgps:home')
    else:
        form = AuthenticationForm()
    return render(request, template_name, {'form': form})

@login_required(login_url='/')
def cadastro_jovem(request):
    return render(request, 'cadastro_jovem.html')

@login_required(login_url='/')
def cadastro_crianca(request):
    return render(request, 'cadastro_crianca.html')

@login_required(login_url='/')
def cadastro_idoso(request):
    return render(request, 'cadastro_idoso.html')

'''
def cadastro(request, template_name='cadastro.html'):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('sgps:home')
    return render(request, template_name, {'form': form})
'''

@login_required(login_url='/')
def listar_jovem(request):
    return render(request, 'listagem_jovens.html')

@login_required(login_url='/')
def listar_crianca(request):
    return render(request, 'listagem_criancas.html')

@login_required(login_url='/')
def listar_idoso(request):
    return render(request, 'listagem_idosos.html')

@login_required(login_url='/')
def suporte(request):
    return render(request, 'suporte.html')

@login_required(login_url='/')
def preferencias(request):
    return render(request, 'preferencias.html')