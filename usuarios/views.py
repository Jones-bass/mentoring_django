from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import auth
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib.auth import authenticate


def cadastro(request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    else:
        email = request.POST.get("email")
        username = request.POST.get("username")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get("confirmar_senha")

    if not senha == confirmar_senha:
        messages.add_message(
            request, constants.ERROR, "Senha e Confimar senha dever iguais."
        )
        return redirect("/usuarios/cadastro")

    if len(senha) < 8:
        messages.add_message(
            request, constants.ERROR, "A senha deve ter no mínimo 8 caracteres."
        )
        return redirect("/usuarios/cadastro")

    users = User.objects.filter(email=email)
    if users.exists():
        messages.add_message(request, constants.ERROR, "Já existe usuário com este E-mail cadastrado.")
        return redirect("/usuarios/cadastro")

    User.objects.create_user(email=email, username=username, password=senha)

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        user_obj = User.objects.filter(email=email).first()
        username = user_obj.username if user_obj else None

        # Passa o username encontrado (ou None) para o autenticador padrão do Django
        user = authenticate(request, username=username, password=senha)

        if user is not None:
            auth.login(request, user)
            return redirect("/passou no login")

        messages.add_message(request, constants.ERROR, "E-mail ou senha inválidos.")
        return redirect("login")