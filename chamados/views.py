from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Chamados
from django.shortcuts import get_object_or_404
from .forms import ChamadoForm
from django.contrib import messages

def listar_chamados(request):
    try:
        chamados = Chamados.objects.all()
    except:
        raise ('Sem chamados')
    return render(request, 'chamados/listar.html', {'chamados': chamados})

def ver_chamado(request, pk):
    try:
        chamado = get_object_or_404(Chamados, pk=pk)
    except:
        raise ('Chamado não encontrado')
    return render(request, 'chamados/ver.html', {'chamado': chamado})

def cadastrar_chamado(request):
    if request.method == 'POST':
        try:
            form = ChamadoForm(request.POST)
        
            if form.is_valid():
                chamado = form.save(commit=False)
                chamado.usuario = request.user
                chamado.save()

                return redirect('listar_chamados')
            else:
                print(form.errors)
        except:
            raise ('Erro ao cadastrar chamado')
    else:
        form = ChamadoForm()
    
    messages.success('Chamado cadastrado com sucesso')

    return render(request, 'chamados/cadastrar.html', {'chamado': chamado})

def editar_chamado(request, pk):
    chamado = get_object_or_404(Chamados, pk = pk)
    if request.method == 'POST' and chamado:
        try: 
            form = ChamadoForm(request.POST, instance=chamado)
            
            if form.is_valid():
                chamado_editado = form.save(commit=False)
                chamado_editado = request.user
                chamado_editado.save()

                return redirect('listar_chamados')
            else:
                print(form.errors)
        except:
            raise ('Erro ao editar chamado')
    else:
        form = ChamadoForm()

    messages.success('Chamado editado com sucesso!')

    return render(request, 'chamados/editar.html', {'chamado': chamado})

def deletar_chamado(request, pk):
    chamado = get_object_or_404(Chamados, pk=pk)

    if chamado:
        titulo = chamado.titulo
        chamado.delete()
    else:
        raise ('Chamado não encontrado')

    messages.success(request, f'Chamado: {titulo} apagado com sucesso')

    return redirect('chamados:listar_chamados')