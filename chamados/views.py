from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Chamados
from django.shortcuts import get_object_or_404

def listar_chamados(request):
    chamados = Chamados.objects.all()
    return render(request, 'chamados/listar.html', {'chamados': chamados})

def ver_chamado(request, pk):
    chamado = get_object_or_404(Chamados, pk=pk)
    return render(request, 'chamados/ver.html', {'chamado': chamado})