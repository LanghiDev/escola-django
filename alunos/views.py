from django.shortcuts import render, redirect
from alunos.models import Aluno
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def login_user(request):
    return render(request, 'index.html')


def logout_user(request):
    logout(request)
    return redirect('/')


@login_required(login_url="/login/")
def lista_alunos(request):
    usuario = request.user
    alunos = Aluno.objects.filter(usuario=usuario)
    dados = {'alunos':alunos}
    return render(request, 'alunos.html', dados)


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        aut = authenticate(username=username, password=password)
        if aut is not None:
            login(request, aut)
    return redirect('/')
