from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages


def cadastro(request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    else:
        username = request.POST.get("username")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get("confirmar_senha")

    if not senha == confirmar_senha:
        messages.add_message(request, constants.ERROR, 'Senha e Confimar senha dever iguais.')
        return redirect("/usuarios/cadastro")

    if len(senha) < 8:
        messages.add_message(request, constants.ERROR, 'A senha deve ter no mínimo 8 caracteres.')
        return redirect("/usuarios/cadastro")

    users = User.objects.filter(username=username)
    if users.exists():
        messages.add_message(request, constants.ERROR, 'Já existe usuário cadastrado.')
        return redirect("/usuarios/cadastro")

    User.objects.create_user(username=username, password=senha)
