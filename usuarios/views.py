from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Usuario
from .forms import UsuarioForm

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/listar.html', {'usuarios': usuarios})

def cadastrar_usuario(request):
    if request == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            try:
                usuario = form.save(commit=False)
                usuario.usuario = request.user
                usuario.save()

                messages.success(request, 'Usuário cadastrado com sucesso!')
                return redirect('usuarios:cadastrar_usuario')
            except:
                messages.error(request, 'Erro ao cadastrar usuário')
        else:
            messages.warning(request, 'Erro, dados inválidos')
    else:
        form = UsuarioForm()
    
    return render(request, 'usuarios/cadastrar.html', {'form': form})

def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk = pk)
    if request == "POST":
        form = UsuarioForm(request.POST, instance = usuario)
        if form.is_valid():
            try:
                usuario = form.sava(commit=False)
                usuario.usuario = request.user
                usuario.save()

                messages.success(request, 'Usuário editado com sucesso!')
                return redirect('usuarios:listar_usuarios')
            except:
                messages.error(request, 'Erro ao editar o usuário')
        else:
            messages.warning(request, 'Erro, dados inválidos')
    else:
        form = UsuarioForm(instance = usuario)
    
    return render(request, 'usuarios/editar.html', {'form': form, 'usuario': usuario})

def deletar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk = pk)

    try:
        usuario.delete()
        messages.success(request, 'Usuário deletado com sucesso!')
    except:
        messages.error(request, 'Erro ao deletar o usuário')
    
    return redirect ('usuarios:listar_usuarios')