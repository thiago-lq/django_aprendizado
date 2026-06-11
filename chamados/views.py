from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Chamados
from .forms import ChamadoForm

@login_required
def listar_chamados(request):
    chamados = Chamados.objects.all()
    return render(request, 'chamados/listar.html', {'chamados': chamados})

@login_required
def ver_chamado(request, pk):
    chamado = get_object_or_404(Chamados, pk=pk)
    return render(request, 'chamados/ver.html', {'chamado': chamado})

@login_required
def cadastrar_chamado(request):
    if request.method == 'POST':
        form = ChamadoForm(request.POST)
        if form.is_valid():
            try:
                chamado = form.save(commit=False)
                chamado.usuario = request.user
                chamado.save()
                messages.success(request, 'Chamado cadastrado com sucesso!')
                return redirect('chamados:listar_chamados')
            except:
                messages.error(request, 'Erro ao cadastrar o chamado.')
        else:
            messages.warning(request, 'Formulário inválido. Verifique os dados.')
    else:
        form = ChamadoForm()

    return render(request, 'chamados/cadastrar.html', {'form': form})

@login_required
def editar_chamado(request, pk):
    chamado = get_object_or_404(Chamados, pk=pk)

    if request.method == 'POST':
        form = ChamadoForm(request.POST, instance=chamado)
        if form.is_valid():
            try:
                chamado_editado = form.save(commit=False)
                chamado_editado.usuario = request.user
                chamado_editado.save()
                messages.success(request, 'Chamado editado com sucesso!')
                return redirect('chamados:listar_chamados')
            except:
                messages.error(request, 'Erro ao editar o chamado.')
        else:
            messages.warning(request, 'Formulário inválido. Verifique os dados.')
    else:
        form = ChamadoForm(instance=chamado)

    return render(request, 'chamados/editar.html', {'form': form, 'chamado': chamado})

@login_required
def deletar_chamado(request, pk):
    chamado = get_object_or_404(Chamados, pk=pk)
    try:
        chamado.delete()
        messages.success(request, 'Chamado deletado com sucesso!')
    except:
        messages.error(request, 'Erro ao deletar o chamado.')

    return redirect('chamados:listar_chamados')