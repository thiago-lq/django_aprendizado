from django.contrib import admin
from .models import Chamados

# Register your models here.

@admin.register(Chamados)
class ChamadosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'usuario', 'setor', 'prioridade', 'data_hora', 'prazo')
    list_filter = ('prioridade', 'setor')
    search_fiels = ('titulo')